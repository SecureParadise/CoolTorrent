# IPv4 Packet Breakdown

**Hexadecimal Packet Data:**


#### 1. Version and IHL (Internet Header Length)
- **Value:** `45`
  - **Version (4 bits):** `4` (IPv4)
  - **IHL (4 bits):** `5` (Header length: 5 x 32-bit words = 20 bytes)

**Explanation:** 
- The packet uses IPv4 with a standard header length of 20 bytes (no options).

#### 2. Type of Service (ToS)
- **Value:** `00`

**Explanation:**
- Default settings with no special handling for delay, throughput, or reliability.

#### 3. Total Length
- **Value:** `00 28`
  - **Decimal:** 40 bytes

**Explanation:**
- Total length of the packet, including header and data, is 40 bytes.

#### 4. Identification
- **Value:** `7f 69`
  - **Decimal:** 32,601

**Explanation:**
- Unique identifier for the packet, typically incremented for each new packet.

#### 5. Flags and Fragment Offset
- **Value:** `40 00`
  - **Flags (3 bits):** `4` (DF flag set)
  - **Fragment Offset (13 bits):** `0000` (Offset is 0)

**Explanation:**
- DF (Don't Fragment) flag indicates the packet should not be fragmented. The fragment offset of 0 shows this packet is not fragmented.

#### 6. Time to Live (TTL)
- **Value:** `80`
  - **Decimal:** 128

**Explanation:**
- TTL value of 128; decremented by each router. If TTL reaches 0, the packet is discarded.

#### 7. Protocol
- **Value:** `06`
  - **Decimal:** 6 (TCP)

**Explanation:**
- Indicates the protocol used in the data part is TCP (Transmission Control Protocol).

#### 8. Header Checksum
- **Value:** `b5 fb`

**Explanation:**
- Checksum for verifying the integrity of the IPv4 header. It’s used to detect errors in the header.

#### 9. Source IP Address
- **Value:** `c0 a8 01 47`
  - **Decimal:** `192.168.1.71`

**Explanation:**
- IP address of the source from which the packet originated.

#### 10. Destination IP Address
- **Value:** `28 4a db 31`
  - **Decimal:** `40.74.219.49`

**Explanation:**
- IP address of the destination to which the packet is being sent.
