#!/usr/bin/env python


from random import randint
import sys

file_name = sys.argv[1]
arg = sys.argv[2]

with open(file_name) as f:
    text = f.read()
    text_thing = text.replace('\n',' ')
    text_list = text_thing.split(' ')


d = dict()
for i in range(len(text_list)-1):
    a = text_list[i]
    b = text_list[i+1]
    if a in d.keys():
        d[a].append(b)
    else:
        d[a] = [b]

def get_word(words):
    word = randint(0,len(words)-1)
    return words[word]

last_word = ''
for i in range(int(arg)):
    if i == 0:
        temp_word = get_word(text_list)
        markov = temp_word
    else:
        temp_word = get_word(d[last_word])
        markov = markov + ' '+ temp_word
    last_word = temp_word
print markov
