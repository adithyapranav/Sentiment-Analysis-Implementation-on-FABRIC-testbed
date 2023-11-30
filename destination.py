from scapy.all import sniff, IP, send, Raw from sklearn.feature_extraction.text import TfidfVectorizer

./receiv

import pandas as pd

import joblib

import ast

myIp = "10.0.3.2" dstIp =

inInterface = "enp7s0"

outInterface = "enp6s0"

def packet_filter(packet):

	if IP in packet and packet [IP].dst == myIp: return True

		else:

	return False


def process_packet(packet):

	print(f"Received packet from (packet[IP].src}:")

	packet.show()

	# Extract payload

	payload = (packet[Raw].load).decode() print(payload) payload = ast.literal_eval(payload) #model filename = 'sentiment_model.joblib' #classifier - joblib.load(model_filename)

	print(payload) print(f"Payload received is (payload)")

	# ML Processing

	# Load the saved vectorizer

	#vectorizer filename = 'tfidf_vectorizer.joblib'

	#vectorizer = joblib.load(vectorizer filename)

	#Make a prediction

	#prediction classifier.predict(payload)

	#print (f"Sentiment Prediction: (prediction)") #newPayload = payload

	#forwardPacket IP(dst-dstip) / newPayload

	# Send payload out of specified interface

	#send(forwardPacket, iface-out Interface, verbose-False) #print (f"Payload sent out of (out Interface)")

def main():

	print("Sniffing for packets...")

	sniff(iface-inInterface, filter "ip", prn-procels packet, ifilter packet filter, store-False)

name main()