# -*- coding: utf-8 -*-
"""DAY 3 entity recognition system.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sAF-tBIR9yMVBlTR6AwSUD4y9fnG3yT4
"""

# prompt: 1.A Python script implementing the entity recognition system

import spacy

# Load a pre-trained spaCy model (you might need to download it first)
# !python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

def recognize_entities(text):
    """
    Recognizes entities in the given text using spaCy.

    Args:
        text (str): The input text.

    Returns:
        list: A list of tuples, where each tuple contains the entity text and its label.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage
text = "Toutche Electric is an Electric Mobility venture, based in Bangalore & Mysore, incorporated in Feb 2018. The venture itself began its journey in 2015 when the founding team of Raghu K (Graduate from IIM Bangalore & NIT Warangal) and Mahesh H.S. (Engineering Graduate from Mysore) started putting the foundational blocks together."
entities = recognize_entities(text)
print(entities)  # Output: [('Apple', 'ORG'), ('U.K.', 'GPE'), ('$1 billion', 'MONEY')]


text = "I want to buy a Heileo X200 electric bicycle."
entities = recognize_entities(text)
print(entities)

text = "What are the features of the Heileo M100?"
entities = recognize_entities(text)
entities