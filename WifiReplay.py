# by 7h30th3r0n3
# License: MIT

from scapy.all import *
from scapy.layers.dot11 import Dot11
import os
import sys
import subprocess

print("WARNING: Ensure your wireless card is in promiscuous mode.")
print("Run 'sudo airmon-ng start wlan0' (or replace 'wlan0' with your interface) before using this script.")

if os.geteuid() != 0:
    print("This script requires sudo privileges. Please run it with sudo.")
    sys.exit(1)

pcap_file = input("Enter the path to the PCAP file: ")

try:
    packets = rdpcap(pcap_file)
except FileNotFoundError:
    print(f"Error: The file '{pcap_file}' does not exist.")
    exit(1)

interfaces = get_if_list()
print("Available network interfaces:")
for idx, iface in enumerate(interfaces):
    print(f"{idx + 1}. {iface}")

while True:
    try:
        interface_idx = int(input("Enter the number corresponding to the network interface (e.g., 1): ")) - 1
        if 0 <= interface_idx < len(interfaces):
            interface = interfaces[interface_idx]
            break
        else:
            print("Error: Please enter a valid number from the list.")
    except ValueError:
        print("Error: Please enter a valid number.")

if interface not in get_if_list():
    print(f"Error: The interface '{interface}' is not available.")
    exit(1)

while True:
    try:
        channel = int(input("Enter the channel number to set (e.g., 6): "))
        if 1 <= channel <= 14:
            result = subprocess.run(['iwconfig', interface, 'channel', str(channel)],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                print(f"Successfully set the channel to {channel} on interface '{interface}'.")
                break
            else:
                print(f"Error setting channel: {result.stderr.decode().strip()}")
        else:
            print("Error: Please enter a valid channel number (1-14).")
    except ValueError:
        print("Error: Please enter a valid number.")

try:
    inter_delay = float(input("Enter the delay (in seconds) between each packet (e.g., 0.1): "))
except ValueError:
    print("Error: Please enter a valid number for the delay.")
    exit(1)

for pkt in packets:
    if pkt.haslayer(Dot11):
        new_pkt = RadioTap() / pkt[Dot11]
        sendp(new_pkt, iface=interface, count=1, inter=inter_delay)

print("Packet replay completed.")

print("Script developed by 7h30th3r0n3")
