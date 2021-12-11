import unittest
from math import gcd
from decimal import *


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if(y == 0):
            print("ERROR: denominator  can't be 0: {}/{}".format(x, y))
        else:
            if(isinstance(x, int) and isinstance(y, int)):
                div = gcd(x, y)
                self.x = x // div
                self.y = y // div
            else:
                tem = x.as_integer_ratio()
                self.x = tem[0]
                self.y = tem[1]

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if(self.y == 1):
            return "{}".format(self.x)
        else:
            return "{}".format(self.x/self.y)
            # return "{}/{}".format(self.x, self.y)

    def __repr__(self):         # zwraca "Frac(x, y)"
        # x = (self.x).as_integer_ratio()
        return "Frac({},{})".format(self.x, self.y)

    # Py2.7 i Py3
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __lt__(self, other):
        return self.x/self.y < other.x/other.y

    def __le__(self, other):
        return self.x/self.y <= other.x/other.y

    # nadmiarowe
    def __gt__(self, other):
        return self.x/self.y > other.x/other.y

    # nadmiarowe
    def __ge__(self, other):
        return self.x/self.y >= other.x/other.y

    def __add__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        result = [int(self.x*other.y + self.y*other.x), int(self.y*other.y)]
        div = gcd(result[0], result[1])
        result[0] = result[0] // div
        result[1] = result[1] // div
        return Frac(result[0], result[1])

    __radd__ = __add__

    def __radd__(self, other):
        result = [int(other*self.y + 1*self.x), int(1*self.y)]
        div = gcd(result[0], result[1])
        result[0] = result[0] // div
        result[1] = result[1] // div
        return Frac(result[0], result[1])

        # int+frac

    def __sub__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        result = [int(self.x*other.y - self.y*other.x), int(self.y*other.y)]
        div = gcd(result[0], result[1])
        result[0] = result[0] // div
        result[1] = result[1] // div
        return Frac(result[0], result[1])

    __rsub__ = __sub__              # int-frac

    def __rsub__(self, other):
        result = [int(other*self.y - 1*self.x), int(1*self.y)]
        div = gcd(result[0], result[1])
        result[0] = int(result[0] / div)
        result[1] = int(result[1] / div)
        return Frac(result[0], result[1])

    def __mul__(self, other):   # frac1*frac2, frac*int
        if isinstance(other, int):
            other = Frac(other, 1)
        result = [int(self.x*other.x), int(self.y*other.y)]
        div = gcd(result[0], result[1])
        result[0] = result[0] // div
        result[1] = result[1] // div
        return Frac(result[0], result[1])

    __rmul__ = __mul__              # int*frac

    def __rmul__(self, other):   # frac1*frac2, frac*int
        result = [int(self.x*other), int(self.y)]
        div = gcd(result[0], result[1])
        result[0] = result[0] // div
        result[1] = result[1] // div
        return Frac(result[0], result[1])

    def __truediv__(self, other):  # frac1/frac2, frac/int, Py3
        if isinstance(other, int):
            other = Frac(other, 1)
        result = [int(self.x*other.y), int(self.y*other.x)]
        div = gcd(result[0], result[1])
        result[0] = result[0] // div
        result[1] = result[1] // div
        return Frac(result[0], result[1])

    __rtruediv__ = __truediv__

    def __rtruediv__(self, other):  # int/frac, Py3
        result = [int(self.x*1), int(self.y*other)]
        div = gcd(result[0], result[1])
        result[0] = result[0] // div
        result[1] = result[1] // div
        return Frac(result[0], result[1])

    # operatory jednoargumentowe

    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):         # -frac = (-1)*frac
        return (-1)*self

    def __invert__(self):      # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return float(self.x/self.y)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])

# Kod testujący moduł.


class TestTime(unittest.TestCase):

    def setUp(self):
        self.f1 = Frac(1, 1)
        self.f2 = Frac(1, 2)
        self.f3 = Frac(1, 0)
        self.f4 = Frac(0.25)

    def test_print(self):      # test str() i repr()
        self.assertEqual(str(self.f1), "1")
        self.assertEqual(str(self.f2), "0.5")
        self.assertEqual(repr(self.f4), "Frac(1,4)")

    def test_cmp(self):
        self.assertTrue(Frac(1, 1) == Frac(1, 1))
        self.assertFalse(Frac(0.25) != Frac(0.25))
        self.assertTrue(Frac(2, 2) > Frac(1, 2))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 2), Frac(0))
        self.assertEqual(Frac(3, 2) - Frac(1, 2), Frac(1, 1))
        self.assertEqual(1 - Frac(1, 2), Frac(1, 2))
        self.assertEqual(Frac(4, 2) - 1, Frac(1, 1))

    def test_add(self):
        self.assertEqual(2 + Frac(1, 2), Frac(5, 2))
        self.assertEqual(Frac(0.25) + Frac(0.25), Frac(1, 2))
        self.assertEqual(Frac(1, 2) + 2, Frac(5, 2))

    def test_mul(self):
        self.assertEqual(3 * Frac(2, 2), Frac(3, 1))
        self.assertEqual(Frac(2, 2) * 3, Frac(3, 1))
        self.assertEqual(Frac(0.25) * Frac(0.25), Frac(1, 16))

    def test_div(self):
        self.assertEqual(3 / Frac(2, 2), Frac(1, 3))
        self.assertEqual(Frac(0.25) / Frac(0.25), Frac(1, 1))

    def test_invert(self):
        self.assertEqual(~Frac(2), Frac(1, 2))


if __name__ == "__main__":
    unittest.main()     # wszystkie testy
