# -*- coding: utf-8 -*-

import os
import numpy as np
import re
import constants as const

pattern = re.compile("[,]")

dirname = os.path.dirname(__file__)
sourceFile = os.path.join(dirname, const.sourceFile)
outFile = os.path.join(dirname, const.chainTable)

#Create ouputs directory if doesn't exist
import pathlib
pathlib.Path(outFile).parent.mkdir(parents=True, exist_ok=True) 

count = np.zeros((const.arraySize, const.arraySize, const.arraySize), dtype='int32')

with open(sourceFile, "r") as lines:
    for line in lines:
        # Split the comma
        word, wordOccStr = pattern.split(line)

        #transform String to Number
        wordOccurences = int(wordOccStr)
        
        #Add a endline symbol to tell the probability that a charater ends a name
        word = word + "\n"
        
        i = 0
        j = 0
        for k in [ord(c) for c in list(word)]:
            count[i, j, k] += wordOccurences
            i = j
            j = k
            
            
count.tofile(outFile)

print ("Finished!")