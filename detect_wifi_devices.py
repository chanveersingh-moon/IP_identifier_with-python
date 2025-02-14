import os
import re

def get_connected_devices():
    devices = []
    output = os.popen("arp -a").read()  # Run arp -a command
    matches = re.findall(r"(\d+\.\d+\.\d+\.\d+)", output)  # Extract IP addresses
    
    for ip in matches:
        if not ip.startswith("192.168.1.1") and ip != "127.0.0.1":  # Ignore router IP & localhost
            devices.append(ip)
    
    print(f"Connected Devices ({len(devices)}):")
    for device in devices:
        print(f"📶 {device}")

get_connected_devices()
