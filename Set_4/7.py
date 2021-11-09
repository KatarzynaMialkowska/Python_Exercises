"""
Program: 
    flatten sequence, import subsquence to main sequence
Author:      
    Katarzyna Miałkowska
"""



def flatten(x):
    result = []
    for i in x:
        if isinstance(i, (list, tuple)):
            result = result + flatten(i)
        else:
            result.append(i)
    return result

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

print(flatten(seq))

