# -*- coding: utf-8 -*-
"""Dialogue Management.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mxsk0DBB4WfrwEyKfNjT2kMsmX-fpOqe
"""

import random

class DialogueManager:
    def __init__(self):
        self.user_intent = None
        self.conversation_history = []
        self.greetings = ["Hello!", "Hi there!", "hi buddy!"]
        self.farewells = ["Goodbye!", "See you later!", "Farewell!"]
        self.unknown_intent = ["I'm sorry, I didn't understand.", "Could you rephrase that?", "I'm not sure what you mean."]

        # Example intents and responses. Expand this as needed.
        self.intents = {
    "greet": ["Hello!", "Hi there!", "hi buddy!"],
    "farewell": ["Goodbye!", "See you later!", "Farewell!"],
    "weather": ["I'm sorry, I cannot provide weather information."],
    "time": ["I'm sorry, I cannot provide time information."],
    "ask_bike_models": ["We offer models X, Y, and Z."],
    "ask_bike_features": ["The Heileo M100 has features A, B and C."],
    "ask_pricing": ["The Heileo X200 costs $1000."],
    "ask_dealer_location": ["You can buy Toutche bikes at store D."],
    "request_test_ride": ["You can schedule a test ride by calling us."],
    "technical_support": ["Please contact our support team for assistance."]
}

    def get_response(self, user_input):
        self.conversation_history.append(user_input)
        self.user_intent = self.determine_intent(user_input)
        if self.user_intent:
          if self.user_intent in self.intents:
            return random.choice(self.intents[self.user_intent])
          else:
            return random.choice(self.unknown_intent)
        else:
          return random.choice(self.unknown_intent)

    def determine_intent(self, user_input):
        user_input = user_input.lower()  # Case-insensitive matching
        if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
            return "greet"
        elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
            return "farewell"
        elif "weather" in user_input:
            return "weather"
        elif "time" in user_input:
            return "time"
        elif "electric bicycle models" in user_input:
            return "ask_bike_models"
        elif "features of Heileo M100" in user_input:
            return "ask_bike_features"
        elif "cost" in user_input and "Heileo X200" in user_input:
            return "ask_pricing"
        elif "buy Toutche bikes" in user_input:
            return "ask_dealer_location"
        elif "test ride" in user_input:
            return "request_test_ride"
        elif "charging" in user_input and "e-bike" in user_input:
            return "technical_support"
        else:
            return None


if __name__ == "__main__":
    manager = DialogueManager()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = manager.get_response(user_input)
        print("Bot:", response)