"""
docs

"""

import pickle
import re
import sys
import math
from nltk.corpus import wordnet


__version__ = '0.1'
__author__ = 'ELI Data Mining Group'

with open('data/lemmatizer.pkl', 'rb') as f:
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

    file_map = {
        'NGSL': 'data/wordlists/ngsl_2k.txt',
        'PET': 'data/wordlists/pet_coca_2k.txt',
        'PELIC': 'data/wordlists/pelic_l3_2k.txt'
    }
    if custom_list is not None:
        if isinstance(custom_list, list):
            raise TypeError('Please specify a list of strings for custom_list')
        common_types = set(custom_list)
    else:
        try:
            with open(file_map[freq_list]) as f:
                common_types = set([x.strip() for x in f.readlines()])
        except KeyError as e:
            raise KeyError \
                ('Please specify an appropriate frequency list with' \
                'custom_list or set freq_list to one of NGSL, PET, PELIC.')


    tokens = re_tokenize(text)
    if len(tokens) == 0:
        return 0

    advanced = set()
    for token in tokens:
        lemma = LOOKUP.get(token, token)
        if lemma not in common_types and (not spellcheck or wordnet.synsets(lemma)):
            advanced.add(lemma)
    return len(advanced)/math.sqrt(len(tokens))
