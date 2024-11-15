# OPC/UA Client Sample Project

This project demonstrates a Python implementation to interact with an OPC/UA server, enabling the reading of tag values in either standard read or subscription modes. The provided code is built using the **asyncua** library, which supports asynchronous communication with OPC/UA servers.

## Project Overview

### Features:
- **Standard Read Mode:** Continuously reads values from a set of nodes on the server at a specified interval.
- **Subscription Mode:** Listens for data changes on specific nodes and logs updates.
- Asynchronous communication ensures efficient handling of server interactions.

### Prerequisites:
1. **Python 3.8+** is required to run this project.
2. Install the **asyncua** library:
   ```bash
   pip install asyncua
   ```
3. Ensure access to an OPC/UA server. The server URL is specified in the code.

---

## Code Walkthrough

### Key Components:
- **Server Connection:**
  The client connects to the server using the `Client` class, with a customizable URL.

- **Namespace Index:**
  The `projectName` variable is used to retrieve the server's namespace index, which helps identify nodes correctly.

- **Nodes to Read:**
  Specify nodes to be read in `nodesToReadStr`. These are provided in the format:
  ```
  ns=<NamespaceIndex>;g=<GUID>
  ```
  Example:
  ```python
  f"ns={idx};g=0bd2dca9-0f76-17ca-c11d-fb328f5d85b6"
  ```

- **Standard Read Loop:**
  The client reads values continuously from the specified nodes and logs the time taken for each read operation.

- **Subscription Mode (Optional):**
  The `SubHandler` class handles data change notifications when subscribing to a node. Uncomment the relevant section to enable this mode.

---

## Usage Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Update Configuration**:
   - Modify the `url` variable to point to your OPC/UA server.
   - Add or remove node strings in the `nodesToReadStr` list to customize which tags are read.

3. **Run the Script**:
   ```bash
   python opcua_reader.py
   ```

4. **Monitor Logs**:
   Output includes:
   - Time taken for each read operation in standard read mode.
   - Data change notifications in subscription mode (if enabled).

---

## Example Output

**Standard Read Mode**:
```
INFO:root:Index of namespace OpcReadTime is 2
ReadMode time: 0:00:00.123456
Value from node ns=2;g=0bd2dca9-0f76-17ca-c11d-fb328f5d85b6: 42
```

**Subscription Mode**:
```
Received value for node ns=2;g=0bd2dca9-0f76-17ca-c11d-fb328f5d85b6: 42
```

---

## Notes

- This code assumes the OPC/UA server supports GUID-based node identification.
- Ensure proper error handling and logging in production environments.
- You can adapt the read interval (`asyncio.sleep`) and subscription update rate as needed.

---

## Future Improvements

- Add enhanced error handling and connection recovery.
- Implement dynamic node discovery to avoid manual node configuration.
- Integrate unit tests for key functions.

Happy coding! 🚀
