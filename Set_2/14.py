"""
Program:    
    Find the longest word in the string return its length.
Author:     
    Katarzyna Miałkowska
"""
from typing import Tuple

def the_longest_word(line: str) -> Tuple[str, int]:
    a = max(line.split())
    b = max(len(w) for w in line.split())
    return  a, b

line = "My name is Olaf"
print("the longest word in the string is {}".format(the_longest_word(line)))
