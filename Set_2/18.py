"""
Program:    
    Find and count elements in number
Author:     
    Katarzyna Miałkowska
"""

def Find_and_count(x: int, y: int) -> int:
    return str(x).count(str(y))


num = 120000120
print("Number of '0' in '{}'".format(num) +" = {}".format(Find_and_count(num, 0)))
