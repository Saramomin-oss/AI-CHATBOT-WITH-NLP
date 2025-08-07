import nltk
import random
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data (only first time)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Response database
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "default": ["I'm sorry, I didn't quite get that. Can you rephrase?"]
}

# Keywords for intent detection
keywords = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you"],
    "thanks": ["thanks", "thank you", "thx"]
}

lemmatizer = WordNetLemmatizer()

# Preprocessing user input
def preprocess(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word not in string.punctuation]
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

# Intent detection
def get_intent(tokens):
    for intent, keys in keywords.items():
        for word in tokens:
            if word in keys:
                return intent
    return "default"

# Generate response
def chatbot_response(user_input):
    tokens = preprocess(user_input)
    intent = get_intent(tokens)
    return random.choice(responses[intent])

# Chat loop
def start_chat():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot:", random.choice(responses["goodbye"]))
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Run chatbot
if __name__ == "__main__":
    start_chat()
