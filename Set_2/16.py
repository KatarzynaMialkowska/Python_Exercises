"""
Program:    
    Replace elements in list,
    example: "GvR" to "Guido van Rossum".
Author:     
    Katarzyna Miałkowska
"""

def replace_L_elements(L: list, x, y) -> list:
    L[:] = [y if e == x else e for e in L] 
    return L


L = [1, "GvR", 3, 2, "GvR"]

print("List : {}".format(L))

print("List : {}".format(replace_L_elements(L, "GvR", "Guido van Rossum")))
