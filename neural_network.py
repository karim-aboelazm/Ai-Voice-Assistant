import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(stm):
    return nltk.word_tokenize(stm)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_stm,words):
    stm_word = [stem(word) for word in tokenized_stm]
    bag = np.zeros(len(words),dtype=np.float32)
    for indx , w in enumerate(words):
        if w in stm_word:
            bag[indx] = 1
    return bag
        