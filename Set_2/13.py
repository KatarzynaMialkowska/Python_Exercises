"""
Program:    
    Find the total length of the words in line. 
Author:     
    Katarzyna Miałkowska
"""


def words_length(line: str) -> int:
    return sum(len(w) for w in line.split())

line = "My name is Olaf"
print("length of the words in line = {}".format(words_length(line)))
