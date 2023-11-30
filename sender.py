om scapy.all import IP, UDP, send

./sender.py

ef sendPacket(targetIp, strMsg="", srcPrt = 12345 dstPrt = 54321 ) :

target_ip = targetIp

source_port = srcPrt destination_port = dstPrt

# Custom message

message = strMsg

# Create the packet

packet = IP(dst=target_ip) / UDP(sport source_port, dport=destination_port) / message

# Send the packet

send(packet, verbose=False) print("Packet sent!")

if name main":

sendPacket C^ prime prime 10 * 0 .2^ prime prime "My name is Rachit")

sendPacket("10.0.0.2", "Nice to meet you.") sendPacket (^ prime prime 10 * 0 .2^ prime prime "What is your Name?")

sendPacket("10.0.0.2", "I love this product, It is amazing.")

sendPacket("10.0.0.2", "I hat this product")

sendPacket (^ prime prime 10 * 0 .2^ prime prime , "I have no comments for this product")