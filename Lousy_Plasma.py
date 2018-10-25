import string
import random

def remove_punctuation(var):
    no_punct = ""
    punctuation =  '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in var: 
        if item not in punctuation:
            no_punct += item + " " 
    return no_punct



f = open('thesaurus.txt', 'r')
syn_dict = {"happy" :["GLAD", "BLISSFUL", "ECSTATIC"], "sad":["BLEAK", "BLUE", "DEPRESSED"]}

syn = {}
for line in f:
    split_words = line.split(',')
    first_val = split_words.pop(0)
    syn.update({first_val:split_words})
print(syn)



def lousy_plasma():
    new_string = ""
    quest = input("What would you like to translate?").strip()
    quest = quest.split()
    quest = remove_punctuation(quest).split()
    for item in quest:
        if item in syn.keys():
            new_string += random.choice(syn[item]) + " "
        else:
            new_string += item + " "

    print(new_string) 
lousy_plasma()

