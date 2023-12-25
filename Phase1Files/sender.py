from scapy.all import IP, UDP, send



def sendPacket(targetIp, strMsg="", srcPrt=12345, dstPrt=54321):
    target_ip = targetIp
    source_port = srcPrt
    destination_port = dstPrt

    # Custom message
    message = strMsg

    # Create the packet
    packet = IP(dst=target_ip) / UDP(sport=source_port, dport=destination_port) / message

    # Send the packet
    send(packet, verbose=False)
    print("Packet sent!")

if __name__ == "__main__":
    sendPacket("10.0.0.2", "My name is Rachit")
    sendPacket("10.0.0.2", "Nice to meet you.")
    sendPacket("10.0.0.2", "What is your Name?")
    sendPacket("10.0.0.2", "I love this product, It is amazing.")
    sendPacket("10.0.0.2", "I hate this product")
    sendPacket("10.0.0.2", "I have no comments for this product")
