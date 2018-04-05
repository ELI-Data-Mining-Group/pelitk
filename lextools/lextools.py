"""
docs

"""


__version__ = '0.1'
__author__ = 'ELI Data Mining Group'

import re
import pickle

LOOKUP = pickle.load('lemmatizer.pkl')
def lemmatize(tokens):
    """ Lemmatize with lookup table and return list of corresponding lemmas """
    return [LOOKUP.get(x, x) for x in tokens]
