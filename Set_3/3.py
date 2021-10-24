"""
Program: 
    Prints the numbers from X to Y in a loop, 
    except for numbers that are divisible by Z. 
Example: 
    X = 0 , Y = 30, Z = 3
Author:     
    Katarzyna Miałkowska
"""

def not_divisible(x: int, y: int, z: int):
    for i in range(x, y+1):
        if (i % z != 0) : print(f"{i}")

not_divisible(0, 30, 3)
