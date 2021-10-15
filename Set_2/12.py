"""
Program:    
    Building a word from the first characters of the words in the line.
    Building a word from the last characters of the words on the line. 
Author:     
    Katarzyna Miałkowska
"""


def word_from_f_chars(line: str) -> str:
    word = ""
    for w in line.split():
        word += w[0]
    
    return word

def word_from_l_chars(line: str) -> str:
    word = ""
    for w in line.split():
        word += w[-1]
    
    return word


line = "My name is Olaf"

print("New word from the first chars = {}".format(word_from_f_chars(line)))

print("New word from the last chars = {}".format(word_from_l_chars(line)))