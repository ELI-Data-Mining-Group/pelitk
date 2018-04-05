"""
docs

"""


__version__ = '0.1'
__author__ = 'ELI Data Mining Group'

import pickle
import re

LOOKUP = pickle.load('lemmatizer.pkl')
def lemmatize(tokens):
    """ Lemmatize with lookup table and return list of corresponding lemmas """
    return [LOOKUP.get(x, x) for x in tokens]


def re_tokenize(text):
    """
    Returns a list of tokens from input text
    Lowercase input, removing symbols and digts.
    """
    return re.findall(r"[A-Za-z]+", text.lower())
