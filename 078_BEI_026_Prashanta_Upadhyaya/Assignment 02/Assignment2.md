

#### Differentiation between OSI & TCP/IP Model:

| **OSI Model** | **TCP/IP Model** |
| ------------- | ----------------- |
| Developed by the International Organization for Standardization (ISO) | Created by the Defense Advanced Research Projects Agency (DARPA) |
| 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application | 4 layers: Network Interface, Internet, Transport, and Application |
| Each layer has a specific role and interacts directly with the layers above and below it | Layers are more flexible and can perform functions that span across multiple OSI layers |
| Layers communicate only with their immediate neighbors | Layers can interact more broadly, allowing for more practical implementation |
| Protocol-independent, serving as a conceptual framework for understanding networking | Built around specific protocols used on the Internet |
| Primarily used as a teaching tool and reference model | Widely adopted and used in real-world networking and the Internet |

#### Differentiation between Peer to Peer Architecture & Client Server Architecture:

| **Peer to Peer (P2P) Architecture** | **Client-Server Architecture** |
| ----------------------------------- | ----------------------------- |
| Each node acts as both a client and a server, sharing resources directly with other peers | Centralized server provides resources and services to multiple clients |
| Highly scalable as each additional peer brings additional resources | Scalability can be limited by the capacity of the central server |
| More reliable as there is no single point of failure | Less reliable due to dependency on the central server; if the server fails, clients cannot access resources |
| Typically lower cost as it doesn't require dedicated servers | Higher cost due to the need for dedicated and potentially expensive server infrastructure |
| More complex management due to the distributed nature | Easier to manage with centralized control over resources and services |

#### Seven Layers of the OSI Model and Functions of Each Layer:

| **Layer**            | **Function** |
| -------------------- | ------------ |
| **Physical Layer**   | Handles the transmission and reception of raw data bits over a physical medium (cables, wireless). Manages hardware elements like cables, switches, and network interface cards (NICs). |
| **Data Link Layer**  | Ensures reliable transmission of data frames between two nodes connected by a physical layer. Handles error detection and correction, and controls how data is placed on the physical layer. |
| **Network Layer**    | Manages the delivery of packets across multiple networks, including routing through intermediate routers. Determines the best path to route the packets. |
| **Transport Layer**  | Provides reliable data transfer services to the upper layers, including error recovery and flow control. Manages end-to-end communication and data integrity. |
| **Session Layer**    | Manages sessions or connections between applications. It establishes, maintains, and terminates connections. Provides synchronization and dialog control. |
| **Presentation Layer** | Translates data between the application layer and the network. Handles data encoding, compression, and encryption. Converts data formats to ensure compatibility between different systems. |
| **Application Layer** | Provides network services directly to end-user applications. It includes protocols like HTTP, FTP, and SMTP. Manages network services such as file transfer, email, and network software services. |

#### Principles behind the OSI Model:

| **Principle**          | **Explanation** |
| ---------------------- | --------------- |
| **Layered Architecture** | The OSI model is based on a layered architecture where each layer has a specific function and communicates only with its adjacent layers. |
| **Encapsulation**      | Each layer adds its own header information to the data from the layer above, creating a protocol data unit (PDU) that is passed down to the next layer. |
| **Modularity**         | Each layer operates independently from the others, allowing for modularity and ease of troubleshooting and updating specific layers without affecting the entire model. |
| **Interoperability**   | The OSI model promotes interoperability between different vendors' network products and technologies by standardizing communication functions. |
| **Abstraction**        | The model abstracts complex networking functions into smaller, more manageable layers, making it easier to understand and implement. |
| **Flexibility**        | The model is designed to be flexible, allowing for the addition of new protocols and technologies without disrupting existing operations. |

