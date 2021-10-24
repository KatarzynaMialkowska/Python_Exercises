"""
Program: 
    The program sums the elements in a sequence list (lists or tuples) 
Author:      
    Katarzyna Miałkowska
"""

def sum_sequence(x: list) -> list:
    return [sum(i) for i in x ]

x = [[],[4],(1,2),[3,4],(5,6,7)]

print(sum_sequence(x))