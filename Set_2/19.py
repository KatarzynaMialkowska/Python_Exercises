"""
Program:    
    Fills one-digit and two-digit numbers with zeros and forms a string.
Author:     
    Katarzyna Miałkowska
"""

def from_L_to_string(L: list) -> str:
    word = ' '.join(str(s) for s in L)
    return word

def Fill_to_3(L: list) -> str:
    L[:] = [str(e).zfill(3) if len(str(e))<3 else e for e in L]
    return from_L_to_string(L)


L = [1, 23, 122, 62, 123]
print("New string = {}".format(Fill_to_3(L)))
