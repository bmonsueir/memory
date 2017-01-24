import numpy as np
from pandas import Series,DataFrame
import pandas as pd
#from models import English, German, Spanish, Russian
import sys,os


title = raw_input("enter book title: ") + ".txt"

# title = 'test1.txt'

print(title)

words = {}
with open('English/' + title, 'r') as f:
        for line in f:
            splitLine = line.split()
            for word in splitLine:
                word = (word.lower().replace('.', '').replace(',','').replace("'s",""))
                try:
                    words[word] += 1
                except KeyError as e:
                    words[word] = 1

#sortWords = sorted(words.items(), key=lambda value: value[1])     
sortedWords = sorted([(value,key) for (key,value) in words.items()], reverse=True)

target = open('hist' + title, 'w')
for entry in sortedWords:
    
    line = (str(entry[1]) + " " +  str(entry[0]))
    # print(line)
    target.write(line)
    target.write("\n")
target.close()