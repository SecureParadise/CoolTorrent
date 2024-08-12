import asyncio
import logging
import struct
from asyncio import Queue
from concurrent.futures import CancelledError

import bitstring

REQUEST_SIZE = 2**14

class ProtocolError(BaseException):
    pass

class PeerConnection:
    def __init__(self, queue: Queue, info_hash, peer_id, piece_manager, on_block_cb=None):
        self.my_state = []
        self.peer_state = []
        self.queue = queue
        self.info_hash = info_hash
        self.peer_id = peer_id
        self.remote_id = None
        self.writer = None
        self.reader = None
        self.piece_manager = piece_manager
        self.on_block_cb = on_block_cb
        self.future = asyncio.ensure_future(self._start())

    async def _start(self):
        while 'stopped' not in self.my_state:
            ip, port = await self.queue.get()
            logging.info(f'Got assigned peer with: {ip}')

            try:
                self.reader, self.writer = await asyncio.open_connection(ip, port)
                logging.info(f'Connection open to peer: {ip}')

                buffer = await self._handshake()

                self.my_state.append('choked')
                await self._send_interested()
                self.my_state.append('interested')

                async for message in PeerStreamIterator(self.reader, buffer):
                    if 'stopped' in self.my_state:
                        break
                    if isinstance(message, BitField):
                        self.piece_manager.add_peer(self.remote_id, message.bitfield)
                    elif isinstance(message, Interested):
                        self.peer_state.append('interested')
                    elif isinstance(message, NotInterested):
                        if 'interested' in self.peer_state:
                            self.peer_state.remove('interested')
                    elif isinstance(message, Choke):
                        self.my_state.append('choked')
                    elif isinstance(message, Unchoke):
                        if 'choked' in self.my_state:
                            self.my_state.remove('choked')
                    elif isinstance(message, Have):
                        self.piece_manager.update_peer(self.remote_id, message.index)
                    elif isinstance(message, KeepAlive):
                        pass
                    elif isinstance(message, Piece):
                        self.my_state.remove('pending_request')
                        self.on_block_cb(
                            peer_id=self.remote_id,
                            piece_index=message.index,
                            block_offset=message.begin,
                            data=message.block)
                    elif isinstance(message, Request):
                        logging.info('Ignoring the received Request message.')
                    elif isinstance(message, Cancel):
                        logging.info('Ignoring the received Cancel message.')

                    if 'choked' not in self.my_state:
                        if 'interested' in self.my_state:
                            if 'pending_request' not in self.my_state:
                                self.my_state.append('pending_request')
                                await self._request_piece()

            except ProtocolError:
                logging.exception('Protocol error')
            except (ConnectionRefusedError, TimeoutError):
                logging.warning('Unable to connect to peer')
            except (ConnectionResetError, CancelledError):
                logging.warning('Connection closed')
            except Exception as e:
                logging.exception('An error occurred')
                await self.cancel()  # Ensure cleanup
                raise e
            finally:
                await self.cancel()  # Ensure cleanup happens even if an error occurs

    async def cancel(self):
        logging.info(f'Closing peer {self.remote_id}')
        if not self.future.done():
            self.future.cancel()
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
        self.queue.task_done()

    async def stop(self):
        self.my_state.append('stopped')
        if not self.future.done():
            self.future.cancel()
        await self.cancel()

    async def _request_piece(self):
        block = self.piece_manager.next_request(self.remote_id)
        if block:
            message = Request(block.piece, block.offset, block.length).encode()
            logging.debug(f'Requesting block {block.offset} for piece {block.piece} of {block.length} bytes from peer {self.remote_id}')
            self.writer.write(message)
            await self.writer.drain()

    async def _handshake(self):
        self.writer.write(Handshake(self.info_hash, self.peer_id).encode())
        await self.writer.drain()

        buf = b''
        tries = 1
        while len(buf) < Handshake.length and tries < 10:
            tries += 1
            buf = await self.reader.read(PeerStreamIterator.CHUNK_SIZE)

        response = Handshake.decode(buf[:Handshake.length])
        if not response:
            raise ProtocolError('Unable to receive and parse a handshake')
        if not response.info_hash == self.info_hash:
            raise ProtocolError('Handshake with invalid info_hash')

        self.remote_id = response.peer_id
        logging.info('Handshake with peer was successful')

        return buf[Handshake.length:]

    async def _send_interested(self):
        message = Interested()
        logging.debug(f'Sending message: {message}')
        encoded_message = message.encode()
        if encoded_message is None:
            raise ProtocolError('Failed to encode Interested message')
        self.writer.write(encoded_message)
        await self.writer.drain()

class PeerStreamIterator:
    CHUNK_SIZE = 10*1024

    def __init__(self, reader, initial: bytes=None):
        self.reader = reader
        self.buffer = initial if initial else b''

    async def __aiter__(self):
        return self

    async def __anext__(self):
        while True:
            try:
                data = await self.reader.read(PeerStreamIterator.CHUNK_SIZE)
                if data:
                    self.buffer += data
                    message = self.parse()
                    if message:
                        return message
                else:
                    if self.buffer:
                        message = self.parse()
                        if message:
                            return message
                    raise StopAsyncIteration()
            except ConnectionResetError:
                logging.debug('Connection closed by peer')
                raise StopAsyncIteration()
            except CancelledError:
                raise StopAsyncIteration()
            except Exception:
                logging.exception('Error when iterating over stream!')
                raise StopAsyncIteration()

    def parse(self):
        header_length = 4

        if len(self.buffer) > 4:
            message_length = struct.unpack('>I', self.buffer[0:4])[0]

            if message_length == 0:
                return KeepAlive()

            if len(self.buffer) >= message_length:
                message_id = struct.unpack('>b', self.buffer[4:5])[0]

                def _consume():
                    self.buffer = self.buffer[header_length + message_length:]

                def _data():
                    return self.buffer[:header_length + message_length]

                if message_id == PeerMessage.BitField:
                    data = _data()
                    _consume()
                    return BitField.decode(data)
                elif message_id == PeerMessage.Interested:
                    _consume()
                    return Interested()
                elif message_id == PeerMessage.NotInterested:
                    _consume()
                    return NotInterested()
                elif message_id == PeerMessage.Choke:
                    _consume()
                    return Choke()
                elif message_id == PeerMessage.Unchoke:
                    _consume()
                    return Unchoke()
                elif message_id == PeerMessage.Have:
                    data = _data()
                    _consume()
                    return Have.decode(data)
                elif message_id == PeerMessage.Piece:
                    data = _data()
                    _consume()
                    return Piece.decode(data)
                elif message_id == PeerMessage.Request:
                    data = _data()
                    _consume()
                    return Request.decode(data)
                elif message_id == PeerMessage.Cancel:
                    data = _data()
                    _consume()
                    return Cancel.decode(data)
                else:
                    logging.info('Unsupported message!')
            else:
                logging.debug('Not enough in buffer in order to parse')
        return None

class PeerMessage:
    Choke = 0
    Unchoke = 1
    Interested = 2
    NotInterested = 3
    Have = 4
    BitField = 5
    Request = 6
    Piece = 7
    Cancel = 8
    Port = 9
    Handshake = None
    KeepAlive = None

    def encode(self) -> bytes:
        pass

    @classmethod
    def decode(cls, data: bytes):
        pass

class Handshake(PeerMessage):
    length = 49 + 19

    def __init__(self, info_hash: bytes, peer_id: bytes):
        if isinstance(info_hash, str):
            info_hash = info_hash.encode('utf-8')
        if isinstance(peer_id, str):
            peer_id = peer_id.encode('utf-8')
        self.info_hash = info_hash
        self.peer_id = peer_id

    def encode(self) -> bytes:
        return struct.pack('>B19sB20s20s', 19, b'BitTorrent protocol', 0, self.info_hash, self.peer_id)

    @classmethod
    def decode(cls, data: bytes):
        if data[0] != 19 or data[1:20] != b'BitTorrent protocol':
            return None
        return cls(data[28:48], data[48:68])

    def __str__(self):
        return f'Handshake: {self.peer_id}'

class KeepAlive(PeerMessage):
    def __str__(self):
        return 'KeepAlive'

class BitField(PeerMessage):
    def __init__(self, bitfield: bitstring.BitArray):
        self.bitfield = bitfield

    def encode(self) -> bytes:
        length = 1 + len(self.bitfield.bytes)
        return struct.pack('>Ib', length, PeerMessage.BitField) + self.bitfield.bytes

    @classmethod
    def decode(cls, data: bytes):
        bitfield = bitstring.BitArray(bytes=data[1:])
        return cls(bitfield)

    def __str__(self):
        return f'BitField: {self.bitfield.bin}'

class Interested(PeerMessage):
    def encode(self) -> bytes:
        return struct.pack('>Ib', 1, PeerMessage.Interested)

    def __str__(self):
        return 'Interested'

class NotInterested(PeerMessage):
    def __str__(self):
        return 'NotInterested'

class Choke(PeerMessage):
    def __str__(self):
        return 'Choke'

class Unchoke(PeerMessage):
    def __str__(self):
        return 'Unchoke'

class Have(PeerMessage):
    def __init__(self, index):
        self.index = index

    def encode(self) -> bytes:
        return struct.pack('>IbI', 5, PeerMessage.Have, self.index)

    @classmethod
    def decode(cls, data: bytes):
        index = struct.unpack('>I', data[1:5])[0]
        return cls(index)

    def __str__(self):
        return f'Have: {self.index}'

class Piece(PeerMessage):
    def __init__(self, index, begin, block):
        self.index = index
        self.begin = begin
        self.block = block

    def encode(self) -> bytes:
        block_length = len(self.block)
        return struct.pack('>IbIII', 9 + block_length, PeerMessage.Piece, self.index, self.begin, block_length) + self.block

    @classmethod
    def decode(cls, data: bytes):
        index = struct.unpack('>I', data[1:5])[0]
        begin = struct.unpack('>I', data[5:9])[0]
        block = data[9:]
        return cls(index, begin, block)

    def __str__(self):
        return f'Piece: {self.index}, {self.begin}, {len(self.block)}'

class Request(PeerMessage):
    def __init__(self, index, begin, length):
        self.index = index
        self.begin = begin
        self.length = length

    def encode(self) -> bytes:
        return struct.pack('>IbIII', 13, PeerMessage.Request, self.index, self.begin, self.length)

    @classmethod
    def decode(cls, data: bytes):
        index = struct.unpack('>I', data[1:5])[0]
        begin = struct.unpack('>I', data[5:9])[0]
        length = struct.unpack('>I', data[9:13])[0]
        return cls(index, begin, length)

    def __str__(self):
        return f'Request: {self.index}, {self.begin}, {self.length}'

class Cancel(PeerMessage):
    def __init__(self, index, begin, length):
        self.index = index
        self.begin = begin
        self.length = length

    def encode(self) -> bytes:
        return struct.pack('>IbIII', 13, PeerMessage.Cancel, self.index, self.begin, self.length)

    @classmethod
    def decode(cls, data: bytes):
        index = struct.unpack('>I', data[1:5])[0]
        begin = struct.unpack('>I', data[5:9])[0]
        length = struct.unpack('>I', data[9:13])[0]
        return cls(index, begin, length)

    def __str__(self):
        return f'Cancel: {self.index}, {self.begin}, {self.length}'
