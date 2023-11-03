from scapy.all import sniff, wrpcap

def packet_callback(packet):
    print(packet.summary())

packets = sniff(iface="lo", count=500, prn=packet_callback)

wrpcap("captured_packets.pcap", packets)
