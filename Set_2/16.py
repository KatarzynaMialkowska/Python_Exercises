"""
Program:    
    Replace elements in list, and in string line
    example: "GvR" to "Guido van Rossum".
Author:     
    Katarzyna Miałkowska
"""

def replace_L_elements(L: list, x, y) -> list:
    L[:] = [y if e == x else e for e in L] 
    return L

def replace_str_elements(line: str, x: str, y: str) -> str:
    return line.replace(x, y)


L = [1, "GvR", 3, 2, "GvR"]

line = "My name is Olaf and i love GvR"

print("List : {}".format(L))

print("List : {}".format(replace_L_elements(L, "GvR", "Guido van Rossum")))

print("String : {}".format(line))
print("String : {}".format(replace_str_elements(line, "GvR", "Guido van Rossum")))
