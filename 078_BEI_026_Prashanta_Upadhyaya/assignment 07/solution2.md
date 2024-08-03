# TCP Header Overview

## Size of TCP Header

The TCP header is typically **20 bytes** (160 bits) long. It can be larger, up to **60 bytes**, if options are included.

## Fields in the TCP Header

1. **Source Port (16 bits)**
   - **Description:** Contains the port number of the sender's application.
   - **Purpose:** Helps the receiver identify which application on the sender’s side sent the data.

2. **Destination Port (16 bits)**
   - **Description:** Contains the port number of the receiver's application.
   - **Purpose:** Indicates which application or service on the receiver’s side should handle the incoming data.

3. **Sequence Number (32 bits)**
   - **Description:** Represents the position of the first byte of data in the segment within the overall data stream.
   - **Purpose:** Ensures data is reassembled correctly and helps in reordering segments.

4. **Acknowledgment Number (32 bits)**
   - **Description:** Contains the sequence number of the next byte that the sender of the ACK expects to receive.
   - **Purpose:** Confirms receipt of data and manages the flow of data between sender and receiver.

5. **Data Offset (4 bits)**
   - **Description:** Indicates where the data begins by specifying the size of the TCP header.
   - **Purpose:** Allows the receiver to determine where the header ends and the data begins.

6. **Reserved (6 bits)**
   - **Description:** Reserved for future use and should be set to zero.
   - **Purpose:** Ensures compatibility with future extensions without disrupting current functionality.

7. **Flags (6 bits)**
   - **Description:** Control flags used to manage the connection. They include:
     - **URG:** Urgent pointer field significant.
     - **ACK:** Acknowledgment field significant.
     - **PSH:** Push function.
     - **RST:** Reset the connection.
     - **SYN:** Synchronize sequence numbers.
     - **FIN:** No more data from the sender.
   - **Purpose:** Controls the state and management of the TCP connection.

8. **Window Size (16 bits)**
   - **Description:** Indicates the size of the sender’s receive window (i.e., how much data it can accept).
   - **Purpose:** Manages flow control to prevent the receiver from being overwhelmed by too much data.

9. **Checksum (16 bits)**
   - **Description:** Used for error-checking of the header and data.
   - **Purpose:** Ensures data integrity by detecting errors during transmission.

10. **Urgent Pointer (16 bits)**
    - **Description:** Points to the sequence number of the byte following urgent data.
    - **Purpose:** Prioritizes urgent data that should be processed immediately.

11. **Options (Variable length)**
    - **Description:** Allows for additional features or parameters.
    - **Purpose:** Provides flexibility for TCP to support various extensions and options.

12. **Padding (Variable length)**
    - **Description:** Added to ensure the TCP header is a multiple of 32 bits.
    - **Purpose:** Aligns the header to a 32-bit boundary for consistency.

13. **Data (Variable length)**
    - **Description:** Contains the actual application data being transmitted.
    - **Purpose:** Carries the payload intended for the receiver.

## Summary

- **TCP Header Size:** Typically 20 bytes, can extend up to 60 bytes with options.
- **Fields:**
  - **Source Port:** Identifies the sender’s application port.
  - **Destination Port:** Identifies the receiver’s application port.
  - **Sequence Number:** Tracks the order of bytes in the data stream.
  - **Acknowledgment Number:** Confirms receipt of data.
  - **Data Offset:** Specifies where the data begins.
  - **Reserved:** Reserved for future use.
  - **Flags:** Controls the connection state (URG, ACK, PSH, RST, SYN, FIN).
  - **Window Size:** Manages flow control.
  - **Checksum:** Checks for errors in the header and data.
  - **Urgent Pointer:** Points to urgent data.
  - **Options:** Allows for additional parameters.
  - **Padding:** Aligns the header.
  - **Data:** Contains the actual payload.

