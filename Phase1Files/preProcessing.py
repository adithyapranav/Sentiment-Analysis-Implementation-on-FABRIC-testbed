from scapy.all import sniff, IP, send, Raw
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import joblib
import ast

myIp = "10.0.3.2"
dstIp = ""
inInterface = "enp7s0"
outInterface = "enp6s0"

def packet_filter(packet):

    if IP in packet and packet[IP].dst == myIp:
        return True
    else:
        return False

def process_packet(packet):
    #print(f"Received packet from {packet[IP].src}:")
    #packet.show()

    # Extract payload
    payload = (packet[Raw].load).decode()
    #print(payload)
    payload = ast.literal_eval(payload)
    #print(payload)
    print(f"Sentiment is {payload}")
    # ML Processing
    #model_filename = 'sentiment_model.joblib'
    #classifier = joblib.load(model_filename)

    # Load the saved vectorizer
    #vectorizer_filename = 'tfidf_vectorizer.joblib'
    #vectorizer = joblib.load(vectorizer_filename)

    # Now you can use the loaded model and vectorizer to make predictions on new data

    # Example: Predict sentiment for a new phrase
    #new_phrase = payload
    #processed_new_phrase = preprocess_text(new_phrase)
    #vectorized_new_phrase = vectorizer.transform([processed_new_phrase])

    # Make a prediction
    #prediction = classifier.predict(payload)

    #print(f"Sentiment Prediction: {prediction}")
    #newPayload = payload

    #forwardPacket = IP(dst=dstIp) / newPayload

    # Send payload out of specified interface
    #send(forwardPacket, iface=outInterface, verbose=False)
    #print(f"Payload sent out of {outInterface}")

def main():
    print("Sniffing for packets...")
    sniff(iface=inInterface, filter="ip", prn=process_packet, lfilter=packet_filter, store=False)

if __name__ == "__main__":
    main()
