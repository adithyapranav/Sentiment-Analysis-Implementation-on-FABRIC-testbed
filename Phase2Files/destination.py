from scapy.all import sniff, IP, send, Raw
import datetime

myIps = ["10.0.3.2", "11.0.3.2", "12.0.3.2"]
dstIp = ""
inInterface1 = "enp9s0"
inInterface2 = "enp8s0"
inInterface3 = "enp7s0"
#outInterface = "enp6s0"

uuidSniffTimeMap = {}

def addCustomIdToPacketPayload(id, payload):
	newPayload = payload + "###" + id
	return newPayload

def getIdAndMessage(msg):
	return msg.split("###")

def packet_filter(packet):

    if IP in packet and packet[IP].dst in  myIps:
        return True
    else:
        return False

def process_packet(packet):
    print(f"Received packet from {packet[IP].src}:")
    #packet.show()

    # Extract payload
    payload =  (packet[Raw].load).decode()
    payload, id = getIdAndMessage(payload)
    uuidSniffTimeMap[id] = datetime.datetime.now()
    print(f"payload is {payload}")

    # ML Processing
    newPayload = payload

    #forwardPacket = IP(dst=dstIp) / newPayload

    # Send payload out of specified interface
    #send(forwardPacket, iface=outInterface, verbose=False)
    #print(f"Payload sent out of {outInterface} to IP {dstIp}")
def main():
    print("Sniffing for packets...")
    sniff(iface=[inInterface1, inInterface2, inInterface3], filter="ip", prn=process_packet, lfilter=packet_filter, store=False, timeout=10)
    print(uuidSniffTimeMap)
if __name__ == "__main__":
    main()
