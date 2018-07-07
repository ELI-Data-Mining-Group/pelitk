__version__ = '0.1'
__author__ = 'ELI Data Mining Group'


def ngrams(tokens, n=1):
    """ Takes list of tokens and returns list of ngrams of size n """

    if n == 1:
        return [[x] for x in tokens]
    elif n < 1:
        raise ValueError('Please specify an integer for n that is greater than 1.')
    ngrams = [tokens[:n]]
    for i in range(0, len(tokens)-n):
        ngrams.append(ngrams[i][1:] + [tokens[i+n]])
    return ngrams


def skip_grams(tokens, n=2, skip=1):
    if skip >= n:
        raise ValueError('Please specify an integer for n that is greater than the one for skip')
    n_grams = ngrams(tokens, n+skip)
    # start with ngrams, then remove successively for skip grams
    for gram in n_grams:
        # wait.. is this how skip grams should work?
