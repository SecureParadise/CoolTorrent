# UDP Header Overview

## Size of UDP Header

The UDP header is **8 bytes** (64 bits) long. It is designed to be simple and has minimal overhead.

## Fields in the UDP Header

1. **Source Port (16 bits)**
   - **Purpose:** Identifies the port number used by the sender's application.
   - **Description:** This field helps the receiver determine which application or service on the sender's side sent the datagram. It allows the receiver to direct the datagram to the appropriate application.

2. **Destination Port (16 bits)**
   - **Purpose:** Identifies the port number used by the receiver's application.
   - **Description:** This field specifies the port number of the application or service on the receiver's side that should handle the incoming datagram. It ensures that the datagram reaches the correct application.

3. **Length (16 bits)**
   - **Purpose:** Indicates the total length of the UDP header and data combined.
   - **Description:** This field specifies the size of the entire UDP packet, including both the header and the data. It helps the receiver determine how much data to expect and manage buffer sizes.

4. **Checksum (16 bits)**
   - **Purpose:** Used for error-checking the header and data.
   - **Description:** This optional field helps detect errors that may have occurred during transmission. In IPv4, it is optional, but in IPv6, it is mandatory. If the checksum is incorrect, the datagram may be discarded by the receiver.

## Summary

- **Size:** The UDP header is 8 bytes (64 bits) long.
- **Fields:**
  - **Source Port:** Identifies the sender's port.
  - **Destination Port:** Identifies the receiver's port.
  - **Length:** Specifies the total length of the UDP packet.
  - **Checksum:** Provides error-checking for header and data (optional in IPv4, mandatory in IPv6).

