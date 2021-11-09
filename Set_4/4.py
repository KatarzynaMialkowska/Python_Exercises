
"""
Program: 
    Iterative fibonacci
Author:      
    Katarzyna Miałkowska
"""

def iterative_fibonacci(n: int):
    if n > 0: 
        a = 0 
        b = 1
        for i in range(0, n):
            t = a + b
            a = b 
            b = t
        return a
    else:
        print("Error value")
        
        
print(iterative_fibonacci(8))
print(iterative_fibonacci(-2))