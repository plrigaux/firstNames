import os
import numpy as np
from numpy.random import choice, seed
import constants as const

####################################
#Configuration parameters
SEED = None
GENERATE_LIMIT = 600 #Number of generated words
NEWLINE = ord("\n") #10
WORD_MIN_LENGTH = 4
WORD_MAX_LENGTH = 12
####################################

seed(SEED)

dirname = os.path.dirname(__file__)
sourceFile = os.path.join(dirname, const.sourceFile)
outfile = os.path.join(dirname, const.outfile)
chainTable = os.path.join(dirname, const.chainTable) 

#Construct a list of original word
import re
pattern = re.compile("[,]")

originalWords = set()
with open(sourceFile, "r") as lines:
    for l in lines:
        l = pattern.split(l)[0]
        originalWords.add(l)


#pull back the markov chain table from file
count = np.fromfile(chainTable, dtype="int32")
count = count.reshape(const.arraySize, const.arraySize, const.arraySize)

s = count.sum(axis = 2)

st = np.tile(s.T, (const.arraySize, 1, 1)).T
p = count.astype('float') / st
p[np.isnan(p)] = 0




# create a container with a set of words
container = {}

a = range(const.arraySize)


while True:
    i = 0
    j = 0
    word = ""

    while True:
        #get a random character according to a defined probability
        randomSample = choice(a, 1, p = p[i, j, :])
        k = randomSample[0]
        if k != NEWLINE:
            word += chr(k)
            i = j
            j = k
        else:
            break

    wordLen = len(word)

    #If not within expected length then skip 
    if wordLen < WORD_MIN_LENGTH or wordLen > WORD_MAX_LENGTH:
        continue

    generatedWordOccurences = container.get(word, 0)

    #Mark words comming from the original list
    if word in originalWords:
        word += "*"

    #Count the number of generated occurences
    container[word] = generatedWordOccurences + 1

    #Stop when we reach the limit
    if len(container) >= GENERATE_LIMIT:
        break

        

outFile = open(outfile, "w")

#Order by words
from collections import OrderedDict
d = OrderedDict(sorted(container.items(), key=lambda t: t[0]))
for w, v in d.items():
    print(w, " - ", v)
    outFile.write(w, )
    outFile.write("\n")

outFile.close()

print(" -------------------------------------------- ")

#Order by generations
d = OrderedDict(sorted(container.items(), reverse=True, key=lambda x: x[1]))
for w, v in d.items():
    print(w, " - ", v)
    if v == 1:
        break