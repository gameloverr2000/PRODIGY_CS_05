import scapy.all as scapy

# Define a function to process each packet
def process_packet(packet):
    # Extract relevant information from the packet
    src_ip = packet[scapy.IP].src
    dst_ip = packet[scapy.IP].dst
    protocol = packet[scapy.IP].proto
    payload = packet[scapy.IP].payload

    # Print the packet information
    print(f"Source IP: {src_ip}")
    print(f"Destination IP: {dst_ip}")
    print(f"Protocol: {protocol}")
    print(f"Payload: {payload}")
    print("\n")

# Define a function to start the packet sniffer
def start_sniffer():
    # Use scapy to sniff packets on the default interface
    sniff(prn=process_packet, store=False)

# Start the packet sniffer
start_sniffer()