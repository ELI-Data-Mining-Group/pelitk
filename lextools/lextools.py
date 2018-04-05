"""
docs

"""

import pickle
import re
from nltk.corpus import wordnet


__version__ = '0.1'
__author__ = 'ELI Data Mining Group'

with open('lemmatizer.pkl', 'rb') as f:
    LOOKUP = pickle.load(f)
def lemmatize(tokens):
    """ Lemmatize with lookup table and return list of corresponding lemmas """
    return [LOOKUP.get(x, x) for x in tokens]


def re_tokenize(text):
    """
    Returns a list of tokens from input text
    Lowercase input, removing symbols and digts.
    """
    return re.findall(r"[A-Za-z]+", text.lower())


def adv_guiraud(text, freq_list='NGSL', custom_list=None, spellcheck=True):
    """
    Calculates advanced guiraud: advanced types / sqrt(number of tokens)
    By default, uses NGSL top 2k words as frequency list
    custom_list is a custom list of common types for frequency list
    """

    if custom_list is not None:
        common_types = list(set(custom_list))
    tokens = re_tokenize(text)
    if len(tokens) == 0:
        return 0

    advanced = set()
    for token in tokens:
        lemma = LOOKUP.get(token, token)
        if lemma not in common_types and (not spellcheck or wordnet.synsets(lemma)):
            advanced.add(lemma)
    return len(advanced)
