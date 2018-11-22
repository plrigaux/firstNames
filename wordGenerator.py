import os
import numpy as np
from numpy.random import choice, seed
#seed(1)
seed()

import constants as const

dirname = os.path.dirname(__file__)
sourceFile = os.path.join(dirname, const.sourceFile)
outfile = os.path.join(dirname, const.outfile)
chainTable = os.path.join(dirname, const.chainTable) 

#Construnct a list of original word
import re
pattern = re.compile("[,]")

originalWords = []
with open(sourceFile, "r") as lines:
    for l in lines:
        l = pattern.split(l)[0]
        originalWords.append(l)


#pull back the markov chain table from file
count = np.fromfile(chainTable, dtype="int32")
count = count.reshape(const.arraySize, const.arraySize, const.arraySize)

s = count.sum(axis = 2)
#print(s)

st = np.tile(s.T, (const.arraySize, 1, 1)).T
p = count.astype('float') / st
p[np.isnan(p)] = 0


K = 100
NEWLINE = ord("\n") #10
WORD_MIN_LENGTH = 4
WORD_MAX_LENGTH = 12


container = {}
for wordLen in range(WORD_MIN_LENGTH, WORD_MAX_LENGTH):
    container[wordLen] = set()

condition = set(range(WORD_MIN_LENGTH, WORD_MAX_LENGTH))

a = range(const.arraySize)


while True:
    i = 0
    j = 0
    word = ""


    while True:
        randomSample = choice(a, 1, p = p[i, j, :])
        k = randomSample[0]
        if k != NEWLINE:
            word += chr(k)
            i = j
            j = k
        else:
            break

    wordLen = len(word)

    s = container.get(wordLen, None)

    if not s is None:
        if len(s) <= K:
            if word in originalWords:
                word += "*"
            s.add(word)
        else:
            condition.discard(wordLen)
            if len(condition) == 0:
                break


flat_list = []
for v in container.values():
    for w in v:
        flat_list.append(w)
        

f = open(outfile, "w")

for w in sorted(flat_list):
        print(w)
        f.write(w, )
        f.write("\n")

f.close()