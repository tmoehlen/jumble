from itertools import permutations
import enchant
import sys

enUSDict = enchant.Dict("en_US")
word = sys.argv[1]
word_list = list(word)
perm = permutations(word_list)

for i in list(perm):
    if enUSDict.check(''.join(i)):
        print(''.join(i))
        break
