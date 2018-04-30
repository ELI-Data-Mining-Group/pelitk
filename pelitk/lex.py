"""
docs

"""

import pickle
import re
import math
import pkgutil
from pkg_resources import resource_filename
from nltk.corpus import wordnet


__version__ = '0.1'
__author__ = 'ELI Data Mining Group'

FILE_MAP = {
    'NGSL': resource_filename('pelitk', 'data/wordlists/ngsl_2k.txt'),
    'PET': resource_filename('pelitk', 'data/wordlists/pet_coca_2k.txt'),
    'PELIC': resource_filename('pelitk', 'data/wordlists/pelic_l3_2k.txt'),
    'NGSL_SUPP': resource_filename('pelitk', 'data/wordlists/ngsl_supplementary.txt')
}


def _load_wordlist(key):
    with open(FILE_MAP[key]) as f_in:
        wordlist = set([x.strip().lower() for x in f_in.readlines()])
    return wordlist
# lookup table created from NGSL and spaCy word lists
LOOKUP = pickle.loads(pkgutil.get_data('pelitk', 'data/lemmatizer.pkl'))
def lemmatize(tokens):
    """ Lemmatize with lookup table and return list of corresponding lemmas """
    return [LOOKUP.get(x, x) for x in tokens]


def re_tokenize(text):
    """
    Returns a list of tokens from input text
    Lowercase input, removing symbols and digits.
    """
    return re.findall(r"[A-Za-z]+", text.lower())


def adv_guiraud(text, freq_list='NGSL', custom_list=None, spellcheck=True, supplementary=True):
    """
    Calculates advanced guiraud: advanced types / sqrt(number of tokens)
    By default, uses NGSL top 2k words as frequency list
    custom_list is a custom list of common types for frequency list
    """


    if custom_list is not None:
        if not isinstance(custom_list, list):
            raise TypeError('Please specify a list of strings for custom_list')
        common_types = set(custom_list)
    else:
        if freq_list not in FILE_MAP:
            raise KeyError \
                    ('Please specify an appropriate frequency list with' \
                    'custom_list or set freq_list to one of NGSL, PET, PELIC.')
        common_types = _load_wordlist(freq_list)
    if supplementary:
        common_types.union(_load_wordlist('NGSL_SUPP'))
    if isinstance(text, str):
        tokens = re_tokenize(text)
    else:
        # already tokens?
        tokens = text

    if len(tokens) == 0:
        return 0

    advanced = set()
    for token in tokens:
        lemma = LOOKUP.get(token, token)
        if lemma not in common_types and (not spellcheck or wordnet.synsets(lemma)):
            advanced.add(lemma)

    return len(advanced)/math.sqrt(len(tokens))
