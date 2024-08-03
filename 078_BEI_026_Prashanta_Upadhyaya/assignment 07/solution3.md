# TCP Packet Analysis

## Captured TCP Packet


## Breakdown of TCP Header Fields

### 1. Source Port

- **Value:** 01 bb
- **Hexadecimal:** 01 bb
- **Decimal:** 443
- **Description:** This field contains the port number used by the sender's application.

### 2. Destination Port

- **Value:** e0 ef
- **Hexadecimal:** e0 ef
- **Decimal:** 57583
- **Description:** This field specifies the port number used by the receiver's application.

### 3. Sequence Number

- **Value:** b7 5f 51 56
- **Hexadecimal:** b7 5f 51 56
- **Relative Sequence number:** Value = 1
- **Decimal:** 3076477270
- **Description:** This field indicates the position of the first byte of data in the segment within the overall data stream.

### 4. Acknowledgment Number

- **Value:** 70 07 8e e2
- **Hexadecimal:** 70 07 8e e2
- **Decimal:** 1879543522
- **Description:** This field contains the sequence number of the next byte that the sender of the ACK expects to receive.

### 5. Data Offset

- **Value:** 8
- **Hexadecimal:** 8
- **Description:** This field specifies the size of the TCP header in 32-bit words. The value `80` indicates that the header is `8 * 4 = 32 bytes` long.

### 6. Reserved

- **Value:** 0
- **Hexadecimal:** 0
- **Description:** Reserved for future use and should be set to zero. The value here is part of the flags and other control fields.

### 7. Flags

- **Value:** 10
- **Hexadecimal:** 10
- **Description:** The flags are part of this byte. In this case:
  - **URG (Urgent):** Not set.
  - **ACK (Acknowledgment):** Set.
  - **PSH (Push):** Not set.
  - **RST (Reset):** Not set.
  - **SYN (Synchronize):** Not set.
  - **FIN (Finish):** Not set.

### 8. Window Size

- **Value:** 4002
- **Hexadecimal:** 4002
- **Decimal:** 16386
- **Description:** Indicates the size of the sender’s receive window (how much data it can accept).

### 9. Checksum

- **Value:** 8c 32
- **Hexadecimal:** 8c 32
- **Decimal:** 35890
- **Description:** Used for error-checking of the header and data.

### 10. Urgent Pointer

- **Value:** 00 00
- **Hexadecimal:** 00 00
- **Decimal:** 0
- **Description:** Points to the sequence number of the byte following urgent data.

### 11. Options (Variable length)

- **Value:** 01 01 05 0a 70 07 8e e1 70 07 8e e2
- **Hexadecimal:** 01 01 05 0a 70 07 8e e1 70 07 8e e2
- **Description:** This field contains TCP options. 


## Mapping to TCP Header Fields

Here’s how each part of the captured TCP packet corresponds to the TCP header fields:

1. **Source Port (16 bits):** 01 bb  (Decimal 443)
2. **Destination Port (16 bits):** e0 ef (Decimal 57583)
3. **Sequence Number (32 bits):** b7 5f 51 56 (Decimal 3076477270)
4. **Acknowledgment Number (32 bits):**  70 07 8e e2 (Decimal 1879543522)
5. **Data Offset (4 bits):** 8 
6. **Reserved (6 bits):** 0
7. **Flags (6 bits):** 10 (ACK set)
8. **Window Size (16 bits):** 4002 (Decimal 16386)
9. **Checksum (16 bits):** 8c 32 (Decimal 35890)
10. **Urgent Pointer (16 bits):** 00 00 (Decimal 0)
11. **Options (Variable length):** 01 01 05 0a 70 07 8e e1 70 07 8e e2
## Summary

The TCP header values from the captured packet can be interpreted to understand the source and destination ports, sequence and acknowledgment numbers, header length, flags, window size, checksum, urgent pointer, and options.


# UDP Packet Analysis

## Captured UDP Packet


## Breakdown of UDP Header Fields

### 1. Source Port

- **Value:** 01 bb
- **Hexadecimal:** 01 bb
- **Decimal:** 443
- **Description:** This field contains the port number used by the sender's application.

### 2. Destination Port

- **Value:** ce 77
- **Hexadecimal:** ce 77
- **Decimal:** 52855
- **Description:** This field specifies the port number used by the receiver's application.

### 3. Length

- **Value:** 00 57
- **Hexadecimal:** 00 57
- **Decimal:** 87
- **Description:** Indicates the total length of the UDP packet, including both the header and the data.

### 4. Checksum

- **Value:** b0 2a
- **Hexadecimal:** b0 2a
- **Decimal:** 45098
- **Description:** Used for error-checking the header and data.

## Mapping to UDP Header Fields

Here’s how each part of the captured UDP packet corresponds to the UDP header fields:

1. **Source Port (16 bits):** 01 bb (Decimal 443)
2. **Destination Port (16 bits):** ce 77 (Decimal 52855)
3. **Length (16 bits):** 00 57 (Decimal 87)
4. **Checksum (16 bits):** b0 2a (Decimal 45098)

## Summary

The UDP header values from the captured packet can be interpreted to understand the source and destination ports, total packet length, and checksum.

