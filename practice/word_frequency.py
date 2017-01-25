from __future__ import division
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
#from models import English, German, Spanish, Russian
import sys,os


title = raw_input("enter book title and directory: ") + ".txt"

# title = 'test1.txt'

print(title)

words = {}
word_count = 0
with open(title, 'r') as f:
        for line in f:
            splitLine = line.split()
            for word in splitLine:
                word_count += 1
                word = (word.lower().replace('.', '').replace(',','').replace("'s",""))
                try:
                    words[word] += 1
                except KeyError as e:
                    words[word] = 1

#sortWords = sorted(words.items(), key=lambda value: value[1])     
sortedWords = sorted([(value,key) for (key,value) in words.items()], reverse=True)
print(word_count)
target = open('words_in_' + title, 'w')
target.write("word, count, percent, cum\n")
cum = 0
for entry in sortedWords:
    word_percent = entry[0]/word_count * 100
    cum += word_percent
    line = (str(entry[1]) + ", " +  str(entry[0]) + ", %.2f" % word_percent + ", %.2f" % cum )
    # print(line)
    target.write(line)
    target.write("\n")
target.close()