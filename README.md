# PELITK: Pitt English Language Institute ToolKit
This python package contains implementations of various lexical sophistication measures (vocD, MTLD, Advanced Guiraud, etc) that are useful for SLA work.
### Installation
`pip install git+https://github.com/ELI-Data-Mining-Group/pelitk.git@master`
### Example Usage
```python
>>> from pelitk import lex
>>> print('AG:', lex.adv_guiraud('hi this is a test string'))
AG: 0.8164965809277261
>>> tokens = lex.re_tokenize('hi this is a test string')
>>> print(tokens)
['hi', 'this', 'is', 'a', 'test', 'string']
>>> print(lex.lemmatize(tokens))
['hello', 'this', 'be', 'a', 'test', 'string']
```


### [Documentation](docs)


### To-Do:
- [x] MTLD
- [ ] HDD
- [x] vocD?
- [x] AG
  - [x] NGSL, PSL3, PET, Custom
- [x] re_tokenize
- [x] lemmatize
- [ ] concgrams
- [x] ngrams
- [ ] concordance
- [ ] skip gram
