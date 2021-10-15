"""
Program:    
    Converting from the list of int+ to the string
Author:     
    Katarzyna Miałkowska
"""

def from_L_to_string(L: list) -> str:
    word = ''.join(str(s) for s in L)
    return word


L = [1, 2, 3, 4, 5, 6]
print("the string is {}".format(from_L_to_string(L)))
