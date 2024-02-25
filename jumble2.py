from itertools import permutations
import enchant
import sys

enUSDict = enchant.Dict("en_US")
for s in filter(lambda w: (enUSDict.check(str(''.join(w)))), set(list(permutations(list(sys.argv[1]))))):
    print(''.join(s))
