"""
Program: 
    The program draws a rectangle n x m in console
Author:      
    Katarzyna Miałkowska
"""

def draw_rectangle(n : int, m : int):
    if(n>0 and m>0):
        s = []
        s.append([]) 

        s1 = "+" * (m+1)
        s2 = "-" * 3
        row_outside = s2.join(s1)
        s1 = "|" * (m+1)
        s2 = " " * 3
        row_inside = s2.join(s1)

        for i in range(n):
            print(row_outside)
            print(row_inside)
            s[0].append(row_outside)
            s[0].append(row_inside)
        print(row_outside)
        s[0].append(row_outside)
        return s
    else:
        print("Error: m or n<=0")
       
draw_rectangle(4, 4)
