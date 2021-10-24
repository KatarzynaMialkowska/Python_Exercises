"""
Program: 
    The program return instersection and union of two strings
    (without repeating)
Author:      
    Katarzyna Miałkowska
"""

def intersection(a: str, b: str) -> str:
    return set(a).intersection(b)

def union(a: str, b: str) -> str:
    return set(a).union(b)

a = "123asd123"
b = "123qwe123"

print(f"a: {a}\nb: {b}")
print(f"intersection: {intersection(a,b)}\nunion: {union(a,b)}")