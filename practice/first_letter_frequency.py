from __future__ import division
import sys,os


direct = raw_input("enter directory: ") 
title = direct + "/words.txt" 

print(title)

letters = {}
word_count = 0
with open(title, 'r') as f:
    
    
    for line in f:
        word_count += 1
        letter = line[0]
        try:
            letters[letter] += 1
        except KeyError as e:
            letters[letter] = 1

#sortWords = sorted(words.items(), key=lambda value: value[1])     
sortedWords = sorted([(value,key) for (key,value) in letters.items()], reverse=True)
print(word_count)
print(letters)
print(sortedWords)
target = open(direct + '/first_letter_frequency.txt', 'w')
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