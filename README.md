[![Build Status](https://travis-ci.org/ELI-Data-Mining-Group/pelitk.svg?branch=master)](https://travis-ci.org/ELI-Data-Mining-Group/pelitk)
# PELITK: Pitt English Language Institute ToolKit

`pelitk` is a python package that contains implementations of various lexical analysis tools that are useful for Second Language Acquisition (SLA) work. These modules can be imported and used in Python. At present, there are two modules available:

1. [`conc.py`](#concpy) - functions for creating concordances to show selected key words in context
2. [`lex.py`](#lexpy) - functions measuring lexical sophistication and diversity using a range of indices

### Folder contents

File               | File type     | Description
:---               | :---          | :---
[`docs`](https://github.com/ELI-Data-Mining-Group/pelitk/tree/master/docs) | folder | contains [`CONC.MD`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/docs/CONC.md) and [`LEX.MD`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/docs/LEX.md)
[`CONC.MD`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/docs/CONC.md) | markdown | describes the [`conc.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/pelitk/conc.py) module
[`LEX.MD`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/docs/LEX.md) | markdown | describes the [`lex.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/pelitk/lex.py) module
[`LICENSE.txt`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/LICENSE) | text | General Public License allowing reproduction but not editing of `pelitk`
[`pelitk`](https://github.com/ELI-Data-Mining-Group/pelitk/tree/master/pelitk) | folder | contains the [`data/wordlists`](https://github.com/ELI-Data-Mining-Group/pelitk/tree/master/pelitk/data) folder and the Python modules [`conc.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/pelitk/conc.py) and [`lex.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/pelitk/lex.py)
[`data/wordlists`](https://github.com/ELI-Data-Mining-Group/pelitk/tree/master/pelitk/data/wordlists) | folder | contains the wordlists required for [`lex.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/pelitk/lex.py)
[`conc.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/pelitk/conc.py) | Python script | Python module for installing concordancing functions
[`lex.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/pelitk/lex.py) | Python script | Python module for installing lexical measurement functions
[`README.md`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/README.md) | markdown | describes `pelitk`
[`requirements.txt`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/requirements.txt) | text | list of the Python modules that need to be installed for `pelitk` to function
[`setup.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/setup.py) | Python script | contains `pelitk` information and code required for installation

<br>

### Installation

To install `pelitk`, enter the following into command line:  

`pip install git+https://github.com/ELI-Data-Mining-Group/pelitk.git@master`

In addition, the following are Python modules required for [`lex.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/pelitk/lex.py):
- [nltk](https://www.nltk.org/)
- [scipy](https://www.scipy.org/)
- [numpy](https://numpy.org/)

<br>

### `conc.py`

Essentially, a concordance is a list of words or phrases from a text, presented with their immediate contexts. Concordancing has long been an integral part of corpus investigations; as John Sinclair describes,  

_"The normal starting point for a corpus investigation is the concordance, which from early days in computing has used the [Key Word In Context (KWIC)] format, where instances of a chosen word or phrase (the NODE) are presented in a layout that aligns occurrences of the node vertically, but otherwise keeps them in the order in which they appear in the corpus."_  

Sinclair (2003, xiii)  

`conc.py` creates a concordance list based on key words in a text, and it has options to allow for greater user flexibility. In the example usage below, there is a short text of two sentences which has been tokenized (split into a list of strings) to analyze the key word _platypus_. The output (presented in two formats) demonstrates how concordance lines provide a useful format for quickly seeing how a word (or phrase) is used in different contexts.

```python
>>> from pelitk import conc
>>> tok_text = ['The', 'key', 'word', 'in', 'this', 'text', 'is', 'the', 'noun', 'platypus', '.',
               'I', 'want', 'to', 'see', 'the', 'cotext', 'every', 'time', 'the', 'word', 'platypus', 'occurs', '.']

>>> print(conc.concordance(tok_text,'platypus',5))
[('this text is the noun', 'platypus', '. I want to see'),
('cotext every time the word', 'platypus', 'occurs .   ')]

>>> print(conc.concordance(tok_text,'platypus',5,pretty=True))
['                   this text is the noun   platypus   . I want to see                         ',
 '              cotext every time the word   platypus   occurs .                                ']
```

<br>

Looking at the function more closely, we see that there are three required arguments and two optional arguments:

Argument | Description
:---     | :---
tok_text | a list of tokenized text or list of tuples, e.g. `['the','word']` or `[('the', 'DT'), ('word', 'NN')]`
node     | the node word or tuple that will be the the focus of concordance lines
num      | the size of the collocation span, i.e. how many words on either side of the node
pos      | optional True/False argument (default is 'False'). Set to 'True' if the tok_text is a list of tuples with POS tags (see example above)
pretty   | optional True/False argument (default is 'False'). If True, the output will be formatted so that all the node words are aligned in each row and joined in a single string.

Returning to the example, we see that we have selected a _span_ of 5 words on either side of the key word (or node), which is a common span size, but which could be increased to allow for greater context. The second output shows the difference when the `pretty` argument is set to 'True'. In the 'pretty' format, it is easier to scan visually, but it is more difficult to further process the data.

It is also possible to use `conc.py` with a _list_ of key words, rather than a single key word. For a demonstration of how to do so, see the [`PELIC_concordancing_tutorial`](https://github.com/ELI-Data-Mining-Group/PELIC_dataset/blob/master/tutorials/PELIC_concordancing_tutorial.ipynb) which compiles a concordance list with a list of nine different verbs.

For more example code and a full description of the functions (including their arguments and sub-functions), see [`CONC.md`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/docs/CONC.md) and [`conc.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/pelitk/conc.py).

<br>

### `lex.py`

There are a number of quantitative measures used for understanding and describing lexical proficiency and development. In particular, many researchers have focused on _lexical sophistication_ (the variation in ‘basic’ and ‘advanced’ words used in a text) and _lexical diversity_ (the percentage of unique words in a text). For a complete discussion of lexical proficiency, see [Leńko-Szymańska (2019)](https://www.routledge.com/Defining-and-Assessing-Lexical-Proficiency-1st-Edition/Lenko-Szymanska/p/book/9780367337926). `lex.py` provides functions to calculate a number of the more commonly used metrics of sophistication and diversity, summarized briefly below.

For example code and a full description of the functions (including their arguments and sub-functions), see [`LEX.md`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/docs/LEX.md) and [`lex.py`](https://github.com/ELI-Data-Mining-Group/pelitk/blob/master/pelitk/lex.py).

<br>

**`adv_guiraud`**  
Calculates Advanced Guiraud (AG):
  - measure of lexical sophistication
  - formula = advanced types / sqrt(number of tokens).
  - By default, the function uses NGSL top 2k words as frequency list of common types to ignore. Optionally, other lists can be used instead.

<br>

**`vocd`**  
Calculates vocD:
  - measure of lexical diversity
  - formula = calculating TTR from a number of random samples then fitting a curve and reporting the parameter value
  - the default requires a minimum text length of 35 words (the default number of sub-samples), though this can be optionally adjusted

<br>

**`ttr`**  
Calculates Type-Token_Ratio (TTR):
  - simple measure of lexical diversity
  - formula = number of types / number of tokens in a text
  - practical to calculate but sensitive to text length (shorter texts have higher TTR)

<br>

**`mtld`**  
Calculates Measure of Textual Lexical Diversity (MTLD):
  - measure of lexical diversity
  - formula = complex sequential analysis of samples, generating a score based on TTR scores in the samples.

<br>

**`maas`**  
Calculates Maas (log 2):
  - measure of lexical diversity
  - formula = TTR with log correction

<br>

### [Documentation](docs)

<br>

[Back to top](#PELITK-Pitt-English-Language-Institute-ToolKit)
