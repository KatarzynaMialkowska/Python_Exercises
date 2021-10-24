"""
Is the code syntax corrected in Python?
Author: 
    Katarzyna Miałkowska
"""

#will compile, but no semicolons are needed
x = 2; y = 3
if (x > y):
    result = x
else:
    result = y

#SyntaxError: invalid syntax
"""
for i in "qwerty": if ord(i) < 100: print (i)
"""
#correct:
for i in "qwerty": 
    if ord(i) < 100: print (i)

for i in "axby": print (ord(i) if ord(i) < 100 else i)
