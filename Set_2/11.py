"""
Program: 
    Split chars of word with '_'
Author: 
    Katarzyna Miałkowska
"""


def spilt_of_chars(w: str) -> str:
    words = "_".join(w)
    return words

word = "Dog"
print("Split chars of word '{}'".format(word) + " with '_' : {}".format(spilt_of_chars(word)))
