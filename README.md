# Pitt English Language Institute toolkit (pelitk)

### Installation
`pip install git+https://github.com/ELI-Data-Mining-Group/lextools.git@master`
### Example Usage
```python
>>> from pelitk import lex
>>> print('AG: ', lex.adv_guiraud('hi this is a test string'))
AG:  0.8164965809277261
>>> tokens = lex.re_tokenize('hi this is a test string')
>>> print(tokens)
['hi', 'this', 'is', 'a', 'test', 'string']
>>> print(lex.lemmatize(tokens))
['hello', 'this', 'be', 'a', 'test', 'string']
```


### [Documentation](docs)


### To-Do:
- [ ] MTLD
- [ ] HDD
- [ ] vocD?
- [x] AG
  - [x] NGSL, PSL3, PET, Custom
- [x] re_tokenize
- [x] lemmatize
- [ ] concgrams
- [ ] ngrams
- [ ] concordance
- [ ] skip gram
- [ ] if putting on PyPi, switch to [RST README](https://gist.github.com/dupuy/1855764)
