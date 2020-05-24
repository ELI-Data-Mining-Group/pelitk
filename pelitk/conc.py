# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'Na-Rae Han, Ben Naismith'

# Series of subfunctions for final 'concordance' function


def get_node(tok_text, node, num, pos=False):
    """
    Find a specific word or tuple, i.e. the node, in a tokenized text.

    Args:
        tok_text : list of tokenized text or list of tuples, e.g. ['the','word'] or [('the', 'DT'), ('word', 'NN')]

        node : node word or tuple that will be the the focus of concordance lines

        num : the size of the collocation span, i.e. how many words on either side of the node

        pos : bool, default False
            Set to True if the tok_text is a list of tuples
    """
    if pos:
        padding = [('', '')] * num  # non-word padding, in the specified size
        padded = padding + tok_text + padding  # pad in front and back
        outlist = []
        for i in range(len(padded)):
            if padded[i] == node:
                outlist.append(
                    ([x[0] for x in padded[i - num:i]], padded[i][0],
                     [x[0] for x in padded[i + 1:i + 1 + num]]))
    else:
        padding = [('')] * num  # non-word padding, in the specified size
        padded = padding + tok_text + padding  # pad in front and back
        outlist = []
        for i in range(len(padded)):
            if padded[i] == node:
                outlist.append(
                    (padded[i - num:i], padded[i], padded[i + 1:i + 1 + num]))
    return outlist


def flatten(outlist):
    """
    Flatten outlist from output of of get_node function, joining each concordance into a three-part tuples

    Args:
        outlist: output of get_node function - list, word, list
    """
    flatlist = []
    for x in outlist:
        flatlist.append((' '.join(x[0]), x[1], ' '.join(x[2])))
    return flatlist


def prettify(flatlist):
    """
    Improve the appearance of the flatlist (output of flattn function) to look like a typical
    concordance with node words aligned in a column and each concordance joined as a single string.

    Args:
        flatlist : the output of the function flatten
    """
    return ['{:>40} {:^12} {:<40}'.format(x, y, z) for (x, y, z) in flatlist]


def concordance(tok_text, node, num, pos=False, pretty=False):
    """
    Combine the three functions get_node, flatten, and optionally prettify
    
    Args:
        tok_text : list of tokenized text or list of tuples, e.g. ['the','word'] or [('the', 'DT'), ('word', 'NN')]

        node : node word or tuple that will be the the focus of concordance lines

        num : the size of the collocation span, i.e. how many words on either side of the node

        pos : bool, default False
            Set to True if the tok_text is a list of tuples
        pretty : bool, default False
            If True, the output will be formatted so that all the node words are aligned in each row and joined in a single string.
            This format is easier for scanning visually, but makes it more difficult to further process the data.
    """
    if not pretty:
        if pos:
            return flatten(get_node(tok_text, node, num, pos=True))
        else:
            return flatten(get_node(tok_text, node, num))
    else:
        if pos:
            return prettify(flatten(get_node(tok_text, node, num, pos=True)))
        else:
            return prettify(flatten(get_node(tok_text, node, num)))
