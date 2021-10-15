"""
Program: 
    Calculating the number of words in the sentence.
Author: 
    Katarzyna Miałkowska
"""


def number_of_words(sentence: str) -> int:
    words = sentence.split()
    #for w in words:
    #    print(w)
    return len(words)

line = "My name is Olaf and \tI'm 29 years old.\nI love my dog."
print("Number of words = {}".format(number_of_words(line)))
