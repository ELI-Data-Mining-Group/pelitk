[Home](../README.md) > lextools
---

# conc.py

from pelitk import conc

### **concordance(tok_text, node, num, pos=False, pretty=False)**
Produce a concordance of a selected word or (word,POS) tuple. Combines three sub functions `get_node`, `flatten`, and `prettify` (optional).

#### **Parameters**:
  - `tok_text`: tokenized text (list of strings) | Example: `['The', 'key', 'word', 'in', 'this', 'text', 'is', 'the', 'noun', 'platypus', '.', 'I', 'want', 'to', 'see', 'the', 'cotext', 'every', 'time', 'the', 'word', 'platypus', 'occurs', '.']`  
  OR  
  tokenized text with POS tags (list of tuples) | Example: `[('The', 'DT'), ('key', 'JJ'), ('word', 'NN'), ('in', 'IN'), ('this', 'DT'), ('text', 'NN'), ('is', 'VBZ'), ('the', 'DT'), ('noun', 'JJ'), ('platypus', 'NN'), ('.', '.'), ('I', 'PRP'), ('want', 'VBP'), ('to', 'TO'), ('see', 'VB'), ('the', 'DT'), ('cotext', 'NN'), ('every', 'DT'), ('time', 'NN'), ('the', 'DT'), ('word', 'NN'), ('platypus', 'NN'), ('occurs', 'VBZ'), ('.', '.')]`
  - `node`: node word or tuple | Example: `'platypus'`
  - `num`: size of the collocation span, i.e. how many words on either side of the node | Example: `5`
  - `pos` (optional, defaults to `False`): bool specifying if the tok_text is a list of tuples | Example: see above
  - `pretty` (optional, defaults to `False`): bool specifying if the output should be formatted with all the node words aligned in the concordance and each concordance joined into a single string | Example: see below

#### **Returns**:
Concordance list for the specified node word

#### **Example 1** (pos=False, pretty=False):

###### **Code**:
```python
tok_text = ['The', 'key', 'word', 'in', 'this', 'text', 'is', 'the', 'noun', 'platypus', '.', 'I', 'want', 'to', 'see', 'the', 'cotext', 'every', 'time', 'the', 'word', 'platypus', 'occurs', '.']
concordance(tok_text,'platypus',5)
```

###### **Output**
```python
[('this text is the noun', 'platypus', '. I want to see'),
('cotext every time the word', 'platypus', 'occurs .   ')]
```

#### **Example 2** (pos=False, pretty=True):

###### **Code**:
```python
concordance(tok_text,'platypus',5,pretty=True)
```

###### **Output**
```python
['                   this text is the noun   platypus   . I want to see                         ',
 '              cotext every time the word   platypus   occurs .                                ']
```

#### **Example 3** (pos=True, pretty=False):

###### **Code**:
```python
tokPOS_text = [('The', 'DT'), ('key', 'JJ'), ('word', 'NN'), ('in', 'IN'), ('this', 'DT'), ('text', 'NN'), ('is', 'VBZ'), ('the', 'DT'), ('noun', 'JJ'), ('platypus', 'NN'), ('.', '.'), ('I', 'PRP'), ('want', 'VBP'), ('to', 'TO'), ('see', 'VB'), ('the', 'DT'), ('cotext', 'NN'), ('every', 'DT'), ('time', 'NN'), ('the', 'DT'), ('word', 'NN'), ('platypus', 'NN'), ('occurs', 'VBZ'), ('.', '.')]
concordance(tokPOS_text,'platypus',5,pos=True,pretty=False)
```

###### **Output**
```python
[('this text is the noun', 'platypus', '. I want to see'),
 ('cotext every time the word', 'platypus', 'occurs .   ')]
```


#### **Example 4** (pos=True, pretty=True):

###### **Code**:
```python
concordance(tokPOS_text,'platypus',5,pos=True,pretty=True)
```

###### **Output**
```python
['                   this text is the noun   platypus   . I want to see                         ',
 '              cotext every time the word   platypus   occurs .                                ']
```


### **Printing concordances**
Print concordance output `(pretty=True)` to a csv file.
```python
to_print = concordance(tok_text,'platypus',5,pretty=True)

with open('concordance.csv', 'w', ) as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for conc in to_print:
        wr.writerow([conc])
```
**Note:** To align all the node words in each row, change the font to Consolas
