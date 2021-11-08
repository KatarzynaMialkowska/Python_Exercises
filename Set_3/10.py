"""
Program: 
    The program convert Roman to Integer
Author:      
    Katarzyna Miałkowska

"""

from numeral import roman2int

def roman_to_int_1(val: str)->int:
    try:
        x = roman2int(val)
        return x
    except ValueError as e:
        print(f"Value error: {e}")

def roman_to_int_2(val: str)->int:
    try:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        count = 0
        for i in range(len(val)):
                if i > 0 and roman[val[i]] > roman[val[i - 1]]:
                    count += roman[val[i]] - 2 * roman[val[i - 1]]
                count += roman[val[i]]
        return count
    except KeyError as e:
        print(f"Value error: {e}")
 

print(f"{roman_to_int_1('IX')}")

print(f"{roman_to_int_2('MXVI')}")

