from scapy.all import sniff, IP, send

myIp = "10.0.1.2"
dstIp = "10.0.2.2"
inInterface = "enp7s0"
outInterface = "enp8s0"

def packet_filter(packet):

    if IP in packet and packet[IP].dst == myIp:
        return True
    else:
        return False

def process_packet(packet):
    print(f"Received packet from {packet[IP].src}:")
    packet.show()

    # Extract payload
    payload =  packet[IP].payload

    # ML Processing
    newPayload = payload

    forwardPacket = IP(dst=dstIp) / newPayload

    # Send payload out of specified interface
    send(forwardPacket, iface=outInterface, verbose=False)
    print(f"Payload sent out of {outInterface} to IP {dstIp}")
def main():
    print("Sniffing for packets...")
    sniff(iface=inInterface, filter="ip", prn=process_packet, lfilter=packet_filter, store=False)

if __name__ == "__main__":
    main()
