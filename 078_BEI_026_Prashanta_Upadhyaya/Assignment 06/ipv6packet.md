# IPv6 Header Overview

## Length of an IPv6 Header
The IPv6 header is always **40 bytes** long. Unlike IPv4, the length of the IPv6 header is fixed and does not vary with options.

## Fields in the IPv6 Header

1. **Version (4 bits)**
   - **Purpose**: Indicates the version of the IP protocol.
   - **Value**: `6` for IPv6.
   - **Explanation**: Specifies that this packet uses IPv6.

2. **Traffic Class (8 bits)**
   - **Purpose**: Differentiates packets based on type of traffic and priority.
   - **Explanation**: Similar to the Type of Service (ToS) field in IPv4, this field is used for Quality of Service (QoS) handling and prioritization.

3. **Flow Label (20 bits)**
   - **Purpose**: Identifies packets that belong to the same flow for efficient handling.
   - **Explanation**: Used to manage packets in a stream that requires consistent handling, such as for real-time applications like video or VoIP.

4. **Payload Length (16 bits)**
   - **Purpose**: Specifies the length of the data portion of the packet, excluding the header.
   - **Explanation**: Allows the receiving system to know how much data is in the packet so it can process it correctly.

5. **Next Header (8 bits)**
   - **Purpose**: Indicates the type of the next header that follows the IPv6 header.
   - **Explanation**: Functions similarly to the Protocol field in IPv4. It tells the system what type of protocol or extension header is next (e.g., TCP, UDP, ICMPv6).

6. **Hop Limit (8 bits)**
   - **Purpose**: Limits the number of hops (routers) a packet can traverse.
   - **Explanation**: Serves the same purpose as the TTL (Time to Live) field in IPv4. It prevents packets from circulating indefinitely if there's a routing loop.

7. **Source Address (128 bits)**
   - **Purpose**: Provides the IP address of the sender.
   - **Explanation**: Specifies the origin of the packet. This address is used to route the packet back to the sender if needed.

8. **Destination Address (128 bits)**
   - **Purpose**: Provides the IP address of the intended recipient.
   - **Explanation**: Specifies where the packet is to be delivered. This address is used to route the packet to its destination.

## Summary
- **Version**: Identifies the IP protocol version (IPv6).
- **Traffic Class**: Used for traffic prioritization and QoS.
- **Flow Label**: Helps in managing packets as part of a flow for consistent handling.
- **Payload Length**: Indicates the length of the data portion.
- **Next Header**: Specifies the type of the next header (protocol or extension).
- **Hop Limit**: Limits the number of hops to prevent infinite loops.
- **Source Address**: IP address of the sender.
- **Destination Address**: IP address of the recipient.
