from scapy.all import sniff, IP, send, Raw
import datetime
from nltk.tokenize import word_tokenize
import pandas as pd
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib

# Define preprocess_text function
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    if pd.isnull(text):
        return ''
    
    # Remove special characters, URLs, and mentions
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize
    words = word_tokenize(text.lower())

    # Remove stop words and lemmatize
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]

    return ' '.join(words)

def predict(new_phrase):
    # Load the saved model
    model_filename = 'sentiment_model.joblib'
    classifier = joblib.load(model_filename)

    # Load the saved vectorizer
    vectorizer_filename = 'tfidf_vectorizer.joblib'
    vectorizer = joblib.load(vectorizer_filename)

    # Now you can use the loaded model and vectorizer to make predictions on new data
    processed_new_phrase = preprocess_text(new_phrase)
    vectorized_new_phrase = vectorizer.transform([processed_new_phrase])

    # Make a prediction
    prediction = classifier.predict(vectorized_new_phrase)
    return prediction

myIps = ["10.0.0.2"]
dstIp = ""
inInterface1 = "ens7"

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
    #print(f"Received packet from {packet[IP].src}:")
    #packet.show()

    # Extract payload
    payload =  (packet[Raw].load).decode()
    payload, id = getIdAndMessage(payload)
    sentimentVal = predict(payload)
    print('Sentiment Value  is ', sentimentVal)
    uuidSniffTimeMap[id] = datetime.datetime.now()
    #print(f"payload is {payload}")

    # ML Processing
    newPayload = payload

    #forwardPacket = IP(dst=dstIp) / newPayload

    # Send payload out of specified interface
    #send(forwardPacket, iface=outInterface, verbose=False)
    #print(f"Payload sent out of {outInterface} to IP {dstIp}")
def main():
    print("Sniffing for packets...")
    sniff(iface=inInterface1, filter="ip", prn=process_packet, lfilter=packet_filter, store=False, timeout=20)
    print(uuidSniffTimeMap)
if __name__ == "__main__":
    main()
