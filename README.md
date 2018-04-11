# lextools

### Installation
`pip install git+https://github.com/ELI-Data-Mining-Group/lextools.git@master`
### Example Usage
```python
>>> from lextools import lextools
>>> print('AG: ', lextools.adv_guiraud('hi this is a test string'))
AG:  0.8164965809277261
>>> tokens = lextools.re_tokenize('hi this is a test string')
>>> print(tokens)
['hi', 'this', 'is', 'a', 'test', 'string']
>>> print(lextools.lemmatize(tokens))
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
- [ ] if putting on PyPi, switch to [RST README](https://gist.github.com/dupuy/1855764)
