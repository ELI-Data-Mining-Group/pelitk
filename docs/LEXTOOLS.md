[Home](README.md) > lextools
---

# lextools

### **re_tokenize(text)**

#### **Parameters**:
  - `text`: Input string | Example: `Hi how are you?`

#### **Returns**:
List of tokens from lowercased input, removing symbols and digits.

#### **Example**:

###### **Code**:
```python
lextools.re_tokenize('Hi how are you?')

```

###### **Output**
```python
['hi', 'how', 'are', 'you']
```

### **lemmatize(tokens)**

#### **Parameters**:
  - `tokens`: List of tokens | Example: `['hi', 'how', 'are', 'you']`

#### **Returns**:
List of lemmas

#### **Example**:

###### **Code**:
```python
lextools.lemmatize(['hi', 'how', 'are', 'you'])

```

###### **Output**
```python
['hello', 'how', 'be', 'you']
```


### **adv_guiraud(text, freq_list='NGSL', custom_list=None, spellcheck=True)**

#### **Parameters**:
  - `text`: Input string | Example: `Hi how are you?`
  - `freq_list` (optional, defaults to `'NGSL'`): Specify list of 2K common types to use for AG. Options include `'NGSL', 'PET', 'PELIC'`. | Example: `'PET'`
  - `custom_list` (optional, defaults to `None`): Specify a custom list of common types to use for AG as a list of lemmas. | Example: `['the', 'be', .....]`
  - `spellcheck` (optional, defaults to `True`): Specify whether or not advanced types should be spell-checked using `wordnet.synsets()`. | Example: `False`


#### **Returns**:
Calculated AG lexical diversity index: `advanced types / sqrt(tokens)`

#### **Example**:
###### **Code**:
```python
lextools.adv_guiraud('Hi how are you doing today?')
```

###### **Output**
```python
0.4082482904638631
```
