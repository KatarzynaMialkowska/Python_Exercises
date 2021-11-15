#from fractions import gcd #not compatible with Python 3.9
from math import gcd

def add_frac(frac1: list, frac2:list) -> list:
	result = [frac1[0]*frac2[1] + frac1[1]*frac2[0], frac1[1]*frac2[1]]
	if result[0] == 0: 
		return [0, 1]
	div = gcd(result[0], result[1])
	result[0] = result[0] / div
	result[1] = result[1] / div
	return result

def sub_frac(frac1: list, frac2:list) -> list:
	result = [frac1[0]*frac2[1] - frac1[1]*frac2[0], frac1[1]*frac2[1]]
	if result[0] == 0: 
		return [0, 1]
	div = gcd(result[0], result[1])
	result[0] = result[0] / div
	result[1] = result[1] / div
	return result

def mul_frac(frac1: list, frac2: list) -> list:
	result = [frac1[0]*frac2[0], frac1[1]*frac2[1]]
	if result[0] == 0: 
		return [0, 1]
	div = gcd(result[0], result[1])
	result[0] = result[0] / div
	result[1] = result[1] / div
	return result

def div_frac(frac1: list, frac2:list) -> list:
	result = [frac1[0]*frac2[1], frac1[1]*frac2[0]]
	if result[0] == 0: 
		return [0, 1]
	div = gcd(result[0], result[1])
	result[0] = result[0] / div
	result[1] = result[1] / div
	return result

def is_positive(frac: list) -> int:
	return (frac[0] > 0 and frac[1] > 0)

def is_zero(frac: list) -> int:
	return (frac[0] == 0)

def cmp_frac(frac1: list, frac2: list) -> int:
	frac = sub_frac(frac1, frac2)
	if is_zero(frac): 
		return 0
	elif is_positive(frac): 
		return 1
	else: 
		return -1

def frac2float(frac: list) -> float:
	return float(frac[0])/float(frac[1])


import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([0, 2], [0, 3]), [0, 1])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([5, 6], [2, 6]), [1, 2])
        self.assertEqual(sub_frac([0, 2], [0, 3]), [0, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([5, 6], [2, 6]), [5, 18])
        self.assertEqual(mul_frac([0, 2], [0, 3]), [0, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac([5, 6], [2, 6]), [5, 2])
        self.assertEqual(div_frac([0, 2], [0, 3]), [0, 1])
        
    def test_is_positive(self):
        self.assertEqual(is_positive([5, 6]), 1)
        self.assertEqual(is_positive([-5, 6]), 0)
        self.assertEqual(is_positive([-5, -6]), 0)
        self.assertEqual(is_positive([0, -6]), 0)
        
    def test_is_zero(self):
        self.assertEqual(is_zero([5, 6]), 0)
        self.assertEqual(is_zero([0, 2]), 1)
        
    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([5, 6], [3, 6]), 1)
        self.assertEqual(cmp_frac([-5, 6], [3, 6]), -1)
        self.assertEqual(cmp_frac([-5, -6], [-5, -6]), 0)
        self.assertEqual(cmp_frac([0, -6], [0, 0]), 0)
        
    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([0, 2]), 0)
        
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()