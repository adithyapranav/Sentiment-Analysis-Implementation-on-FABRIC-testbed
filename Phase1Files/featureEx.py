from scapy.all import sniff, IP, send, Raw
import nltk
import ast
import joblib


myIp = "10.0.2.2"
dstIp = "10.0.3.2"
inInterface = "enp7s0"
outInterface = "enp8s0"

def packet_filter(packet):

    if IP in packet and packet[IP].dst == myIp:
        return True
    else:
        return False

def process_packet(packet):
    print(f"Received packet from {packet[IP].src}:")
    #packet.show()

    # Extract payload
    payload =  (packet[Raw].load).decode()
    #print(payload)
    #payload  = ast.literal_eval(payload)
    print(payload)
    model_filename = "sentiment_model.joblib"
    classifier = joblib.load(model_filename)
    vectorizer_filename ="tfidf_vectorizer.joblib"
    vectorizer = joblib.load(vectorizer_filename) 
    #processed_new_phrase = preprocess_text(payload)
    vectorized_new_phrase = vectorizer.transform([payload])
    prediction = classifier.predict(vectorized_new_phrase)
    print(prediction)
    newPayload = str(prediction)
    forwardPacket = IP(dst=dstIp) / newPayload

    # Send payload out of specified interface
    send(forwardPacket, iface=outInterface, verbose=False)
    print(f"Payload sent out of {outInterface}")

def main():
    print("Sniffing for packets...")
    sniff(iface=inInterface, filter="ip", prn=process_packet, lfilter=packet_filter, store=False)

if __name__ == "__main__":
    main()
