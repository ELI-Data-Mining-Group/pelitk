# PELITK: Pitt English Language Institute ToolKit
This python package contains implementations of various lexical analysis tools that are useful for SLA work.

- Tokenization
- Lemmatization
- Measuring lexical sophistication and diversity
- Concordancing

### Installation
`pip install git+https://github.com/ELI-Data-Mining-Group/pelitk.git@master`


### Requirements
Python modules:
- nltk
- scipy
- numpy


### Example Usage
```python
>>> from pelitk import lex
>>> print('AG:', lex.adv_guiraud('hi this is a test string'))
AG: 0.8164965809277261
>>> tokens = lex.tokenize('hi this is a test string')
>>> print(tokens)
['hi', 'this', 'is', 'a', 'test', 'string']
>>> print(lex.lemmatize(tokens))
['hello', 'this', 'be', 'a', 'test', 'string']
```
