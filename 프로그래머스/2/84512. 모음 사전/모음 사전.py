from itertools import product

def solution (word):
    words = ['A', 'E', 'I','O','U']
    dict = []

    for i in range (5):
        for w in product(words, repeat = i+1):
            dict.append(''.join(w))
            dict.sort ()

    return dict. index (word) +1