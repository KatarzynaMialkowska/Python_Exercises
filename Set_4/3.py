
"""
Program: 
    Iterative factorial
Author:      
    Katarzyna Miałkowska
"""

def iterative_factorial(n: int):
    if n > 1: 
        f = 1
        for i in range(1, n+1):
            f = f * i
        return f
    else:
        print("Error value")
        
        
print(iterative_factorial(3))
print(iterative_factorial(-2))