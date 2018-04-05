"""
going to make a package similar to elitools but for lexical processing called lextools:
MTLD
HDD
AG
NGSL, PSL3, PET, Custom
re_tokenize
lemmatize
bandify
6-tuple (in, adv, misspelled)
NGSL, PSL3, PET

"""


__version__ = '0.1'
__author__ = 'ELI Data Mining Group'

from spacy.lang.en import LOOKUP
import re

def lemmatize(tokens):
    """ Lemmatize with lookup table and return list of corresponding lemmas """
    return [LOOKUP.get(x, x) for x in tokens]
