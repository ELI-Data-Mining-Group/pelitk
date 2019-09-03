# -*- coding: utf-8 -*-
import pickle
import re
import math
import random
import pkgutil
from pkg_resources import resource_filename

from nltk.corpus import wordnet
from scipy.optimize import curve_fit
import numpy as np

__version__ = '0.1'
__author__ = 'Pitt ELI Data Mining Group'

FILE_MAP = {
    'NGSL': resource_filename('pelitk', 'data/wordlists/ngsl_2k.txt'),
    'PVL': resource_filename('pelitk', 'data/wordlists/pet_coca_2k.txt'),
    'PSL3_EDM': resource_filename('pelitk', 'data/wordlists/psl3_2k_edm.txt'),
    'PSL3_IJLCR': resource_filename('pelitk', 'data/wordlists/psl3_2k_ijlcr.txt'),
    'SUPP': resource_filename('pelitk', 'data/wordlists/supplementary.txt'),
    'ENABLE1': resource_filename('pelitk', 'data/wordlists/enable1.txt'),
    'OVERLAP': resource_filename('pelitk', 'data/wordlists/overlap.txt'),
    'PSL3_ONLY': resource_filename('pelitk', 'data/wordlists/psl3_only.txt'),
    'PVL_ONLY:' resource_filename('pelitk', 'data/wordlists/pvl_only.txt')
}
# lookup table created from NGSL and spaCy word lists
LOOKUP = pickle.loads(pkgutil.get_data('pelitk', 'data/lemmatizer.pkl'))


def _load_wordlist(key):
    with open(FILE_MAP[key]) as f_in:
        wordlist = set([x.strip().lower() for x in f_in.readlines()])
    return wordlist


def lemmatize(tokens):
    """
    Lemmatize with lookup table and return list of corresponding lemmas

    Args:
        tokens: A list of token strings
    Returns:
        List of lemmas in same order
    """
    return [LOOKUP.get(x, x) for x in tokens]


def re_tokenize(text):
    """
    Regular expression tokenizer. Lowercases input and removes symbols/digits.

    Args:
        text: An input string
    Returns:
        List of tokens found in input string
    """
    return re.findall(r"[A-Za-z]+", text.lower())


def adv_guiraud(text, freq_list='NGSL', custom_list=None,
                spellcheck=True, supplementary=True, lemmas=False):
    """
    Calculates advanced guiraud: advanced types / sqrt(number of tokens)
    By default, uses NGSL top 2k words as frequency list
    custom_list is a custom list of common types for frequency list

    Args:
        text: Input string to calculate AG for
        freq_list: string specifying which freq list to use. Must be one
                   of {'NGSL', 'PET', 'PELIC', 'SUPP'}
        custom_list: if not None, used instead of freq_list (can pass own list
                     of strings containing common types to ignore for AG
        spellcheck: Boolean flag to ignore misspelled words (rough spellcheck
                    with enable1 + 'i' + 'a')
        supplementary: Include NGSL supplementary vocabulary in addition to
                       specified list
    Returns:
        Calculated AG
    """

    if custom_list is not None:
        if not isinstance(custom_list, list):
            raise TypeError("Please specify a list of strings for custom_list")
        common_types = set(custom_list)
    else:
        if freq_list not in FILE_MAP:
            raise KeyError("""Please specify an appropriate frequency list with
                              custom_list or set freq_list to one of NGSL, PET,
                              PSL3_EDM, PSL3_IJLCR.""")
        common_types = _load_wordlist(freq_list)
    # Include supplementary
    if supplementary:
        common_types = common_types.union(_load_wordlist('SUPP'))

    dictionary = _load_wordlist('ENABLE1')
    dictionary.add('i')
    dictionary.add('a')

    if isinstance(text, str):
        tokens = re_tokenize(text)
    else:
        # already tokens?
        tokens = text

    if len(tokens) == 0:
        return 0

    if isinstance(tokens[0], list):
        res = []
        # tokens is a list of lists of tokens
        for toks in tokens:
            advanced = set()
            for token in toks:
                if not lemmas:
                    lemma = LOOKUP.get(token, token)
                else:
                    lemma = token
                if lemma not in common_types:
                    if spellcheck:
                        if lemma in dictionary:
                            advanced.add(lemma)
                    else:
                        advanced.add(lemma)

            res.append(len(advanced) / math.sqrt(len(toks)))
        return res
    else:
        advanced = set()
        for token in tokens:
            if not lemmas:
                lemma = LOOKUP.get(token, token)
            else:
                lemma = token
            if lemma not in common_types:
                if spellcheck:
                    if lemma in dictionary:
                        advanced.add(lemma)
                else:
                    advanced.add(lemma)

        return len(advanced) / math.sqrt(len(tokens))




def _estimate_d(N, TTR):
    """
    Finds value for D to fit to curve, minimizing squared error
    """
    # initial guess of 100 for D
    popt, _ = curve_fit(_vocd_eq, N, TTR, p0=[100])
    return popt[0]


def _vocd_eq(N, D):
    """
    Equation for approximating TTR as function of N and D as described at
    http://www.leeds.ac.uk/educol/documents/00001541.htm
    """
    return D / N * (np.sqrt(1 + 2 * N / D) - 1)


def vocd(text, spellcheck=False, length_range=(35, 50),
         num_subsamples=100, num_trials=3):
    """
    Calculate 'D' with voc-D method (approximation of HD-D)
    Inspired by
    https://metacpan.org/pod/release/AXANTHOS/Lingua-Diversity-0.07/lib/Lingua/Diversity/VOCD.pm

    Args:
        text:
    """
    tokens = [x for x in re_tokenize(
        text) if not spellcheck or wordnet.synsets(LOOKUP.get(x, x))]
    if len(tokens) < length_range[1]:
        raise ValueError("""Sample size greater than population!. Either reduce
                            the bounds of length_range or try a different
                            text.""")
    total_d = 0
    for i in range(num_trials):
        # calculate a D value each trial and average them all
        ttr_list = []
        n_list = []
        for sample_size in range(length_range[0], length_range[1] + 1):
            total_ttr = 0
            for j in range(num_subsamples):
                total_ttr += ttr(random.sample(tokens, sample_size))
            avg_ttr = total_ttr / num_subsamples
            ttr_list.append(avg_ttr)
            n_list.append(sample_size)
        D = _estimate_d(np.array(n_list), np.array(ttr_list))
        total_d += D
    avg_d = total_d / num_trials
    return avg_d


def ttr(tokens):
    """
    Calculate Type-Token Ratio
    """
    return len(set(tokens)) / len(tokens)


def mtld(text, spellcheck=False, factor_size=0.72):
    """
    Implements the Measure of Textual Lexical Diversity (MTLD)
    """
    tokens = [x for x in re_tokenize(
        text) if not spellcheck or wordnet.synsets(LOOKUP.get(x, x))]
    forward_factor_count = _mtld_pass(tokens, factor_size)
    backward_factor_count = _mtld_pass(tokens[::-1], factor_size)
    if forward_factor_count == 0 or backward_factor_count == 0:
        raise ValueError("""Text ttr never fell below the specified
                            factor_size. Try increasing factor_size parameter
                            or using input with more repeated tokens. """)
    mtld = (len(tokens) / forward_factor_count +
            len(tokens) / backward_factor_count) / 2
    return mtld


def _mtld_pass(tokens, factor_size):
    """
    Helper function for mtld, computing one pass of mtld with given tokens.
    """
    current_idx = 0
    factor_count = 0
    for i in range(1, len(tokens) + 1):
        this_slice = tokens[current_idx:i]
        this_ttr = ttr(this_slice)
        if this_ttr < factor_size:
            factor_count += 1
            current_idx = i
    # account for remainder factor count
    if this_ttr > factor_size:
        factor_count += (1.0 - this_ttr) / (1.0 - factor_size)
    return factor_count


def maas(text, spellcheck=False):
    """
    Compute the a^2 Maas index.
    """
    tokens = [x for x in re_tokenize(
        text) if not spellcheck or wordnet.synsets(LOOKUP.get(x, x))]
    num_tokens = len(tokens)
    num_types = len(set(tokens))
    a_squared = math.log(num_tokens) - \
        math.log(num_types) / math.log(num_tokens)**2
    return a_squared
