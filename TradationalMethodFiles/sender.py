from scapy.all import IP, UDP, send
import itertools
import sys
import uuid
import datetime

uuidSentTimeMap = {}

def addCustomIdToPacketPayload(id, payload):
	newPayload = payload + "###" + id
	return newPayload

def getIdAndMessage(msg):
	return msg.split("###")

def sendPacket(targetIp, strMsg, srcPrt=12345, dstPrt=54321, iface=None):
    target_ip = targetIp
    source_port = srcPrt
    destination_port = dstPrt
    
	# Generate a unique ID, for example, a UUID
    custom_id = str(uuid.uuid4())

    # Custom message
    message = addCustomIdToPacketPayload(custom_id, strMsg)

    # Create the packet
    packet = IP(dst=target_ip) / UDP(sport=source_port, dport=destination_port) / message

    # Send the packet on the specified interface
    send(packet, iface=iface, verbose=False)
    uuidSentTimeMap[custom_id] = datetime.datetime.now()
    print(f"Packet sent to {target_ip} on interface {iface} with message: '{strMsg}'")

if __name__ == "__main__":
    # Check if sufficient arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <IP1>")
        sys.exit(1)

    # IP address for the outgoing interfaces
    ip = sys.argv[1]

    # List of messages
    messages = [
    "The sun is shining so brightly this morning!",
    "It's another regular day at the office.",
    "I woke up feeling a bit under the weather today.",
    "Just finished reading an amazing book.",
    "Spent the evening doing routine household chores.",
    "The cake I baked didn't turn out as expected.",
    "Took a refreshing walk in the park.",
    "Watched some TV; it was just okay.",
    "Had a disagreement with a friend.",
    "The weather is just perfect for a picnic.",
    "Found a new café, it was pretty standard.",
    "The birds were unusually loud and disruptive today.",
    "Got a new plant for my collection.",
    "Saw an average sunset this evening.",
    "Had a less than productive day at work.",
    "Made a new recipe, and it was a success!",
    "Went on an ordinary bike ride.",
    "Struggled to take a nap because of the noise.",
    "The stars are so bright tonight.",
    "Received a regular report at work.",
    "Burnt the chocolate I was melting for a recipe.",
    "Listened to my favorite song on repeat.",
    "Had a standard cup of coffee this morning.",
    "Felt a bit stiff and sore after yoga today.",
    "The air smells so fresh after the rain.",
    "Found a podcast; it was neither good nor bad.",
    "Received some constructive criticism at work.",
    "My houseplants are thriving.",
    "Saw a faint rainbow, but it quickly faded.",
    "The bookshop didn't have the novel I wanted.",
    "Enjoyed a relaxing bubble bath.",
    "Just a usual day with my cat.",
    "Skipped breakfast due to running late.",
    "Found a comfy new sweater.",
    "The morning coffee was just like any other day.",
    "The comedy show wasn't as funny as I hoped.",
    "The homemade bread came out just right.",
    "Had a quiet moment, but it was somewhat dull.",
    "It started raining during my walk.",
    "The new art exhibit was inspiring.",
    "Tried a new ice cream flavor; it was okay.",
    "The library was closed when I went.",
    "Found a perfect gift for my friend.",
    "The kids played in the yard, nothing unusual.",
    "Couldn't find a comfortable reading spot.",
    "The morning jog left me feeling energized.",
    "Cooked a meal, it was average.",
    "Didn't see anything interesting at the park.",
    "The flowers I received are so lovely.",
    "Had a day off, but didn't do much."
]


    # Interfaces corresponding to each IP (Replace with actual interface names)
    interface = "ens7"
    for msg in messages:
        sendPacket(ip, msg, iface=interface)
    print(uuidSentTimeMap)
