from itertools import groupby
from operator import itemgetter
exp66word = ['this','is','war']
for letter, words in groupby(sorted(exp66word), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)
