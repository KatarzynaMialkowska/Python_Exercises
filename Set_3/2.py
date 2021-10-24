"""
What's wrong with the code? 
Author: 
    Katarzyna Miałkowska
"""

#Here we sort a new instance (None) 
#L = [3, 5, 4] ; L = L.sort()
L = [3, 5, 4] ; L.sort()
print(L)

#ValueError: too many values to unpack (expected 2) 
#x, y = 1, 2, 3
x, y, z = 1, 2, 3
print(x, y, z)

#TypeError: 'tuple' object does not support item assignment (immutable)
#X = 1, 2, 3 ; X[1] = 4
X = 1, 2, 3
Y = list(X)
Y[1] = 4
X = tuple(Y)
print(X)

#IndexError: list assignment index out of range 
#X = [1, 2, 3] ; X[3] = 4
X = [1, 2, 3, 5] ; X[3] = 4
print(X)

#AttributeError: 'str' object has no attribute 'append'
#X = "abc" ; X.append("d")
X = "abc" ; X += "d"
print(X)

#TypeError: pow() missing required argument 'exp' (pos 2)
#L = list(map(pow, range(8)))
L = list(map(pow, [1,2,3], range(8)))
print(L)