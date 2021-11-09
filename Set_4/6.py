
"""
Program: 
    sum sequence where cen be sub sequence
Author:      
    Katarzyna Miałkowska
"""



def sum_seq(x):
    result = 0
    for i in x:
        if isinstance(i, (list, tuple)):
            result = result + sum_seq(i)
        else:
            result = result + i
    return result

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

print(sum_seq(seq))