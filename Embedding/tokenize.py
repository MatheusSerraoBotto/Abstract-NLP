import os
from pymongo import MongoClient
from nltk.tokenize import word_tokenize
import pickle5 as pickle
from gensim.utils import simple_preprocess

import nltk
nltk.download('punkt')

def pre_process_sentences(sentence: str):
    abstract = simple_preprocess(sentence)
    abstract = word_tokenize(sentence.lower())
    abstract = filter(lambda word: word.isalnum(), abstract)
    return list(abstract)

def get_collection(collection_name: str = 'abstracts'):
    client = MongoClient(os.environ['DB_CONN_STRING'])
    return client['test'][collection_name]

def tokenize_senteces():
    # Tokenization of each document
    sentences = get_collection().find()
    tokenized_sent = []
    for s in sentences:
        abstract = pre_process_sentences(s['abstract'])
        tokenized_sent.append((s['title'], s['theme'], abstract))
    return tokenized_sent



dbfile = open('tokens', 'ab')
pickle.dump(tokenize_senteces(), dbfile)
dbfile.close()