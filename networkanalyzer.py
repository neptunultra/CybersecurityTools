import scapy.all as scapy

def packet_analyzer(packet):
    # Check if the packet is an IP packet
    if packet.haslayer(scapy.IP):
        # Get the source and destination IP addresses
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst

        # Check if the packet is a TCP packet
        if packet.haslayer(scapy.TCP):
            # Get the source and destination port numbers
            src_port = packet[scapy.TCP].sport
            dst_port = packet[scapy.TCP].dport

            # Print the packet information
            print(f"IP Packet: {src_ip} -> {dst_ip}")
            print(f"TCP Packet: {src_port} -> {dst_port}")

        # Check if the packet is a UDP packet
        elif packet.haslayer(scapy.UDP):
            # Get the source and destination port numbers
            src_port = packet[scapy.UDP].sport
            dst_port = packet[scapy.UDP].dport

            # Print the packet information
            print(f"IP Packet: {src_ip} -> {dst_ip}")
            print(f"UDP Packet: {src_port} -> {dst_port}")

        # Check if the packet is an ICMP packet
        elif packet.haslayer(scapy.ICMP):
            # Get the ICMP type and code
            icmp_type = packet[scapy.ICMP].type
            icmp_code = packet[scapy.ICMP].code

            # Print the packet information
            print(f"IP Packet: {src_ip} -> {dst_ip}")
            print(f"ICMP Packet: Type {icmp_type}, Code {icmp_code}")

    # Check if the packet is an ARP packet
    elif packet.haslayer(scapy.ARP):
        # Get the ARP operation
        arp_op = packet[scapy.ARP].op

        # Print the packet information
        print(f"ARP Packet: Operation {arp_op}")

def main():
    # Start sniffing packets
    scapy.sniff(prn=packet_analyzer, store=False)

if __name__ == "__main__":
    main()