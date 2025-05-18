import spacy
import random

# Load spaCy English model (download if needed)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Responses dictionary
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase?", "I don't understand."]
}

# Keywords for intents
keywords = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"],
    "thanks": ["thanks", "thank you"]
}

def classify(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc]
    for intent, keys in keywords.items():
        if any(key in tokens for key in keys):
            return intent
    return "default"

def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        intent = classify(user_input)
        print("Chatbot:", random.choice(responses[intent]))

if __name__ == "__main__":
    chatbot()
