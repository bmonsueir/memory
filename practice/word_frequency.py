from __future__ import division
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
#from models import English, German, Spanish, Russian
import sys,os
import re


direct = raw_input("enter language: ")
title = raw_input("enter book title: ")
file_to_open = direct + "/" + title  + ".txt"
words = {}
word_count = 0
with open(file_to_open, 'r') as f:
        for line in f:
            splitLine = line.split()
            for word in splitLine:
                word_count += 1
                # pattern = 'r"[a-zA-Z]+"g'
                # word = re.match(pattern, word)
                word = re.sub(r"[<>?`~.,&%$#@!*+='-1234567890(){}\[\]]+", '', word)
                word = word.lower()
                try:
                    words[word] += 1
                except KeyError as e:
                    words[word] = 1

    
sortedWords = sorted([(value,key) for (key,value) in words.items()], reverse=True)
print(word_count)
target = open(direct + "/" +'words_in_' + title + ".txt", 'w')
target.write("index, word, count, percent, cum\n")
cum = 0
i = 1
for entry in sortedWords:
    word_percent = entry[0]/word_count * 100
    cum += word_percent
    line = (str(i) + ", " + str(entry[1]) + ", " +  str(entry[0]) + ", %.2f" % word_percent + ", %.2f" % cum )
    i += 1
    target.write(line)
    target.write("\n")
target.close()

