
 # Wireless Packet Replay Tool

This script is a tool designed for replaying 802.11 wireless packets from a provided PCAP file. 

It utilizes the Scapy library and requires a wireless card that supports promiscuous mode. 

## Features
- Reads packets from a PCAP file.
- Allows the user to select a wireless interface and channel.
- Sends 802.11 packets contain in the pcap on the selected channel with a customizable delay between each packet.

---

## Requirements
1. **Python 3.x**
2. **Scapy Library**  
   Install it using `pip install scapy`.
3. **Linux Environment**  
   The script requires Linux with tools like `iwconfig` and `airmon-ng`.
4. **Root Privileges**  
   The script must be run as root (e.g., using `sudo`).

---

## Usage Instructions

### 1. Prepare Your Environment
Ensure your wireless interface is in **promiscuous mode**:
```bash
sudo airmon-ng start wlan0
```
Replace `wlan0` with the name of your wireless interface.

### 2. Run the Script
Execute the script with root privileges:
```bash
sudo python3 replay_packets.py
```

### 3. Follow the Prompts
- Provide the **path** to the PCAP file containing the packets to replay.
- Select the **network interface** to use for packet transmission.
- Specify the **channel number** for the wireless interface.
- Define the **delay** between packet transmissions (in seconds).

### Example Execution
```text
Enter the path to the PCAP file: captured_packets.pcap
Available network interfaces:
1. wlan0
2. eth0
Enter the number corresponding to the network interface (e.g., 1): 1
Enter the channel number to set (e.g., 6): 6
Enter the delay (in seconds) between each packet (e.g., 0.1): 0.2
Packet replay completed.
```

---

## Script Flow
1. **Check for Root Privileges**  
   The script ensures it is run with `sudo`.
2. **Load PCAP File**  
   It attempts to read the provided PCAP file. If the file does not exist, it exits with an error.
3. **Select Network Interface**  
   Lists available interfaces and lets the user select one for packet transmission.
4. **Set Wireless Channel**  
   Uses `iwconfig` to configure the channel for the selected interface.
5. **Replay Packets**  
   Replays 802.11 packets on the selected channel with a user-defined delay.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Warning
**This tool is for educational and ethical purposes only.**  
Unauthorized use of this script to interfere with wireless networks is illegal and unethical. Always ensure you have proper authorization before conducting any wireless testing.

---

### Author
Developed by **7h30th3r0n3**.
