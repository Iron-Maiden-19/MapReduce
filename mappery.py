#!/usr/bin/env python3.6

import sys
import string
 
line = sys.stdin.readline()
#pattern to check for all words with no whitespace in them
vowels = ['a', 'e', 'i', 'o', 'u']
while line:
    line=line.lower()
    line = line.replace(',',' ').replace(';',' ').replace('"',' ').replace('?',' ').replace('.',' ').replace('!',' ').replace("'", "")
    for word in line.split(" "):
        new_word = ""
        for char in word:
            new_word = new_word + char if char in vowels else new_word
                                     
        output= str(new_word)  +"\t" +str(1)
        print(output)       
    line = sys.stdin.readline()    
