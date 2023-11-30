from scapy.all import sniff, IP, send, Raw

import re

myIp =^ prime prime 10.0.0.2^ prime prime

dstIp =^ prime prime 1 theta. theta.1.2^ prime prime inInterface = "enp7s0"

outInterface = Box^ prime prime enD 850^ prime prime

def packet_filter(packet):

if IP in packet and packet[IP].dst = myIp:

return True

else:

return False

def process_packet(packet): print(f"Received packet from (packet[IP].src):")

#packet.show()

of

# Extract payload

go

payload = (packet [Raw].load).decode() print(payload)

go

print(type(payload))

#ML Processing

go

payload re.sub(r'http\S+',", payload)

go

payload = re.sub(r'@[A-Za-z0-9]+',, payload)

go

go

payload = re.sub(r' [^a-zA-Z\s],, payload)

newPayload-payload

print("new payload ", newPayload) forwardPacket IP(dst=dstIp) / newPayload

# Send payload out of specified interface

send(forwardPacket, iface-out Interface, verbose=False) print(f"Payload sent out of (out Interface) to IP (dstIp)")

go