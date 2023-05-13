# Introduction

This notebook demonstrates how to use natural language processing (NLP) to parse a resume and extract relevant information. The notebook is divided into two parts:

- Part 1: This part of the notebook shows how to use the spaCy library to tokenize a resume and extract named entities.
- Part 2: This part of the notebook shows how to use the TextBlob library to extract sentiment scores from a resume.

## Part 1: Tokenization and Named Entity Recognition

The first step in parsing a resume is to tokenize it. Tokenization is the process of breaking a text into individual words or tokens. In this notebook, we will use the spaCy library to tokenize the resume.

To tokenize a resume, we can use the following code:

Code snippet
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Load the resume text
with open("resume.txt", "r") as f:
    resume_text = f.read()

# Tokenize the resume text
resume_tokens = nlp(resume_text)
Use code with caution. Learn more
Once the resume has been tokenized, we can use the spaCy library to extract named entities. Named entities are words or phrases that refer to specific people, places, or things. In this notebook, we will extract the following types of named entities:

Person names: These are the names of people.
Organization names: These are the names of organizations, such as companies, schools, and government agencies.
Job titles: These are the titles of jobs, such as "Software Engineer" or "Manager".
To extract named entities, we can use the following code:

Code snippet
for token in resume_tokens:
    if token.is_named_entity:
        print(token.text, token.label_)
Use code with caution. Learn more
This code will print out all of the named entities in the resume, along with their labels.

## Part 2: Sentiment Analysis

The second step in parsing a resume is to extract sentiment scores. Sentiment analysis is the process of determining the emotional tone of a text. In this notebook, we will use the TextBlob library to extract sentiment scores from a resume.

To extract sentiment scores, we can use the following code:

Code snippet
from textblob import TextBlob

# Create a TextBlob object from the resume text
blob = TextBlob(resume_text)

# Print the sentiment score of the resume
print(blob.sentiment.polarity)
Use code with caution. Learn more
This code will print out the sentiment score of the resume, which is a number between -1 and 1. A score of -1 indicates a negative sentiment, a score of 0 indicates a neutral sentiment, and a score of 1 indicates a positive sentiment.

Conclusion

This notebook has demonstrated how to use NLP to parse a resume and extract relevant information. The notebook is divided into two parts:

Part 1: This part of the notebook shows how to use the spaCy library to tokenize a resume and extract named entities.
Part 2: This part of the notebook shows how to use the TextBlob library to extract sentiment scores from a resume.
