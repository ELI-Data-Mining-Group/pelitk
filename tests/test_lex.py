import math
import random

import pytest

from pelitk import lex

LONG_TEXT = 'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “ and what is the use of a book,” thought Alice, “ without pictures or conversations ?” So she was considering in her own mind, (as well as she could, for the hot day made her feel very sleepy and stupid,) whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a white rabbit with pink eyes ran close by her.'
LONG_TOKENS = lex.re_tokenize(LONG_TEXT)
random.seed(0)

def test_re_tokenize():
    assert False
    input_str = 'hi this is a test string'
    expected_tokens = ['hi', 'this', 'is', 'a', 'test', 'string']

    assert lex.re_tokenize(input_str) == expected_tokens

    input_with_num = 'test input6 with numb3rs'
    expected_tokens = ['test', 'input', 'with', 'numb', 'rs']
    assert lex.re_tokenize(input_with_num) == expected_tokens

    input_all_num = '19382 38749 8'
    expected_tokens = []
    assert lex.re_tokenize(input_all_num) == expected_tokens


def test_adv_guiraud():
    input_str = 'hi this is a test string'
    tokens = lex.re_tokenize(input_str)
    # expect 'test' and 'string' to be advanced types
    assert pytest.approx(lex.adv_guiraud(tokens), 2 / math.sqrt(6))

    input_str_zero_ag = 'this is the'
    tokens_str_zero_ag = lex.re_tokenize(input_str_zero_ag)
    assert lex.adv_guiraud(tokens_str_zero_ag) == 0

    input_str_spell = 'this is a missspellingg'
    tokens_str_spell = lex.re_tokenize(input_str_spell)
    # test w/ spellcheck (misspelling is removed)
    assert lex.adv_guiraud(input_str_spell) == 0
    # test w/o spellcheck
    assert lex.adv_guiraud(tokens_str_spell, spellcheck=False) == 1 / math.sqrt(4)


def test_vocd():
    assert pytest.approx(lex.vocd(LONG_TOKENS)) == 83.399341

    assert pytest.approx(lex.vocd(LONG_TOKENS, spellcheck=True)) == 132.035466


def test_ttr():
    text = 'one two two three'
    tokens = lex.re_tokenize(text)
    assert lex.ttr(tokens) == 3 / 4

    text = 'all unique tokens'
    tokens = lex.re_tokenize(text)
    assert lex.ttr(tokens) == 1


def test_mtld():
    assert pytest.approx(lex.mtld(LONG_TOKENS)) == 78.277031


def test_maas():
    assert pytest.approx(lex.maas(LONG_TOKENS)) == 4.5336033
    assert pytest.approx(lex.maas(LONG_TOKENS, spellcheck=True)) == 4.125937


