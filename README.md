# pelitk: Pitt English Language Institute ToolKit
This python package contains implementations of various lexical analysis tools that are useful for SLA work.

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
>>> tokens = lex.re_tokenize('hi this is a test string')
>>> print(tokens)
['hi', 'this', 'is', 'a', 'test', 'string']
```

```python
>>> from pelitk import conc
>>> tok_text = ['The', 'key', 'word', 'in', 'this', 'text', 'is', 'the', 'noun', 'platypus', '.', 'I', 'want', 'to', 'see', 'the', 'cotext', 'every', 'time', 'the', 'word', 'platypus', 'occurs', '.']
>>> print(conc.concordance(tok_text,'platypus',5))
[('this text is the noun', 'platypus', '. I want to see'),
('cotext every time the word', 'platypus', 'occurs .   ')]
```


### [Documentation](docs)
