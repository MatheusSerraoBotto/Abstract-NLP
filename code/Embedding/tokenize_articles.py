import os
import pickle
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('punkt')


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from gensim.utils import simple_preprocess


stop_words = set(stopwords.words('english')) 

path="./sheets"
csvs = os.listdir(path)
tokenized_sent = []

def pre_process_sentences(sentence: str):
    abstract = word_tokenize(sentence) # Todas as palavras em minusculo
    abstract = [w for w in abstract if not w in stop_words] 
    abstract = filter(lambda word: word.isalpha(), abstract) # Permitir apenas palavras que contenham caracteres alfa
    abstract = filter(lambda word: len(word) > 2 and len(word) < 15, abstract) # Permitir apenas palavras que contenham caracteres alfa
    return list(abstract)

for csv_name in csvs:
    df = pd.read_csv(f'{path}/{csv_name}')
    theme = csv_name[:-4]
    for index, row in df.iterrows():
        try:
            abstract = pre_process_sentences(row['abstract'])
        except:
            continue
        tokenized_sent.append((row['title'], theme, abstract))
    #     break
    # break
        
dbfile = open('tokens_v2', 'ab')
pickle.dump(tokenized_sent, dbfile)
dbfile.close()