
"""
Program: 
    Swap in List from left to rigth iterative and recursive
Author:      
    Katarzyna Miałkowska
"""

def i_swap_in_list(L: list, left: int, rigth:int):
    r = rigth
    for i in range(left, rigth-left):
        t = L[i]
        L[i]=L[r]
        L[r]=t
        --r
    return L

def r_swap_in_list(L: list, left: int, rigth:int):
    if left == rigth:
        return L
    else:
        a = L[left]
        b = L[rigth]
        a, b = b, a
    return r_swap_in_list(L,left+1, rigth-2)
        
        
L = ['1', '2', '3', '4', '5']
print(i_swap_in_list(L, 1, 3))
print(r_swap_in_list(L, 1, 4))