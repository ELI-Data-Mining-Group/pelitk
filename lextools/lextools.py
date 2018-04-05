"""
docs

"""


__version__ = '0.1'
__author__ = 'ELI Data Mining Group'

import pickle
import re

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


def adv_guiraud(freq_list='NGSL', custom_list=None):
    """
    Calculates advanced guiraud: sqrt(advanced types / number of tokens)
    By default, uses NGSL top 2k words as frequency list
    custom_list is a custom list of common types for frequency list
    """

    if custom_list is not None:
        common_types = list(set(custom_list))
