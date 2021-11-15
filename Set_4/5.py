
"""
Program: 
    Swap in List from left to rigth iterative and recursive
Author:      
    Katarzyna Miałkowska
"""

def i_swap_in_list(L: list, left: int, rigth:int):
    while rigth > left :
        a = L [left]
        b = L[rigth]
        L[left] = b
        L[rigth] = a
        left = left + 1
        rigth = rigth - 1
    return L

def r_swap_in_list(L: list, left: int, rigth:int):
    if left > rigth:
        return L
    else:
        a = L [left]
        b = L[rigth]
        L[left] = b
        L[rigth] = a  
        return r_swap_in_list(L,left+1, rigth-1)
        
        
L1 = ['1', '2', '3', '4', '5']
L2 = ['1', '2', '3', '4', '5']
print(i_swap_in_list(L1, 1, 2))
print(r_swap_in_list(L2, 1, 2))