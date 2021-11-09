
"""
Program: 
    The program draws a ruler with the given start and end point in the console
    The program draws a rectangle n x m in console
Author:      
    Katarzyna Miałkowska
"""

def draw_ruler(start : int, end : int): 
    if(start<end):
        s = []
        s.append([])

        end+=1
        s1 = "." * (len(str(end))+2)
        s2 = "|" * (end-start)
        s3 = s1.join(s2)
        start_space = ' '*(len(str(start))-1) #here we can change ' ' to '.' but i prefer this
        s3 = ''.join((start_space,s3))
        print(s3)
 
        s4 = ""
        for i in range(start, end):
            s4 += (str(i) + (' ' * ( len(s1) - len(str(i+1)) + 1 )))
            print(f"{i}{' ' * ( len(s1) - len(str(i+1)) + 1 )}",end='')
        print('')
        s[0].append(s3)
        s[0].append(s4)  
        return s  
    else:
        print("Error: start > end")

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
       
       
s = []
s.append([])
s = draw_ruler(0, 12)
print(s[0][0])
print(s[0][1])
draw_rectangle(4, 4)
