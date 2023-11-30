

yIp =^ prime prime 10.0.1.2"

dstIp =^ prime prime 10.0.2.2^ prime prime

inInterface ="enp8s theta^ prime prime outInterface ="enp7s0"

def packet_filter(packet):

if IP in packet and packet [IP].dst == myIp: return True

else:

return False

def process_packet(packet):

print(f"Received packet from (packet[IP].src}:") packet.show()

# Extract payload

payload = packet[Raw].load.decode()

#ML Processing

payload = word_tokenize(payload.lower())

payload=[lemmatizer.lemmatize(word) for word in payload if word not in stop_words] newPayload = '.join(payload)

#newPayload =str(payload)

forwardPacket = IP(dst-dstIp) / newPayload

#Send payload out of specified interface

send(forwardPacket, iface-out Interface, verbose=False) print(f"Payload sent out of (outInterface)")

def main():

print("Sniffing for packets...")

sniff(iface=inInterface, filter="ip", prn-process_packet, lfilter-packet_filter, store

if name main() main":