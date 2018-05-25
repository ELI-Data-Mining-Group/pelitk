[Home](README.md) > lex
---

# lex

### **re_tokenize(text)**

#### **Parameters**:
  - `text`: Input string | Example: `Hi how are you?`

#### **Returns**:
List of tokens from lowercased input, removing symbols and digits.

#### **Example**:

###### **Code**:
```python
lex.re_tokenize('Hi how are you?')

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
lex.lemmatize(['hi', 'how', 'are', 'you'])

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
lex.adv_guiraud('Hi how are you doing today?')
```

###### **Output**
```python
0.4082482904638631
```

### **vocd(text, spellcheck=True, length_range=(35,50), num_subsamples=100, num_trials=3)**

#### **Parameters**:
  - `text`: Input string | Example: `Hi how are you?`
  - `spellcheck` (optional, defaults to `True`): Specify whether or not advanced types should be spell-checked using `wordnet.synsets()`. | Example: `False`
  - `length_rage` (optional, defaults to (35, 50)): A tuple with the lower and upper bounds of random sample size for vocd
  - `num_subsamples` (optional, defaults to 100): A positive integer specifying how many times to randomly sample the text
  - `num_trials` (optional, defaults to 3): Number of times to average D estimate over

#### **Returns**:
Estimated "D" parameter for the voc-D lexical diversity index

#### **Example**:
###### **Code**:
```python
text = 'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “ and what is the use of a book,” thought Alice, “ without pictures or conversations ?” So she was considering in her own mind, (as well as she could, for the hot day made her feel very sleepy and stupid,) whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a white rabbit with pink eyes ran close by her.'
lex.vocd(text, spellcheck=False)
```

###### **Output**
```python
83.757961976435737
```
