import os
import re
import requests

# Function to get connected devices (IP & MAC addresses)
def get_connected_devices():
    devices = []
    
    # Run 'arp -a' to list connected devices
    output = os.popen("arp -a").read()

    # Extract IP and MAC addresses using regex
    matches = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]+)", output)

    for ip, mac in matches:
        if not ip.startswith("192.168.1.1") and ip != "127.0.0.1":  # Ignore router IP & localhost
            devices.append((ip, mac.upper()))

    return devices

# Function to get device manufacturer from MAC address
def get_mac_vendor(mac_address):
    try:
        url = f"https://api.macvendors.com/{mac_address}"  # Free API to get vendor
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except:
        pass
    return "Unknown"

# Main function to display devices with vendor details
def scan_network():
    devices = get_connected_devices()
    
    print("\n🔍 Connected Devices on Your WiFi:\n")
    for ip, mac in devices:
        vendor = get_mac_vendor(mac)  # Get device manufacturer
        print(f"📶 IP: {ip} | 🆔 MAC: {mac} | 🔹 Device: {vendor}")

scan_network()
