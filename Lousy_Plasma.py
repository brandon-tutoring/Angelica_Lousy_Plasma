import string
import random


def remove_punctuation(var):
    no_punct = ""
    punctuation =  '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in var: 
        if item not in punctuation:
            no_punct += item 
    return no_punct


bad_blood_lyrics = open('bad_blood_lyrics.txt', 'r').read()
f = open('thesaurus.txt', 'r')

syn = {}
for line in f:
    line = line.strip('\n')
    split_words = line.split(',')
    first_val = split_words.pop(0)
    for i in range(0, len(split_words)):
        split_words[i] = split_words[i].upper()
    syn.update({first_val:split_words})

# No longer in use.
'''def lousy_plasma():
    user_input = input("What would you like to translate?").strip()
    user_input_without_punct = remove_punctuation(user_input).split()
    result = ""
    for item in user_input_without_punct:
        if item in syn.keys():
            result += random.choice(syn[item]) + " "
        else:
            result += item + " "
    return result '''


def word_changer(words):
    words = words.strip()
    words_without_punct = remove_punctuation(words).split()
    result = ""
    c = 0
        
    for item in words_without_punct:
        if item in syn.keys():
            if c % 2 == 0:
                result += random.choice(syn[item])
            else: 
                result += item
            c += 1
        else:
                result += item 
        result += " " 
    return result

print(word_changer(bad_blood_lyrics))

