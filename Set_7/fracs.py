import unittest
from decimal import *


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        try:
            if(y == 0):
                raise ValueError
            else:
                self.x = x
                self.y = y
        except ValueError:
            print("ERROR: denominator  can't be 0: {}/{}".format(x, y))

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if(self.y == 1):
            return "{}".format(self.x)
        else:
            return "{}".format(self.x/self.y)
            # return "{}/{}".format(self.x, self.y)

    def __repr__(self):         # zwraca "Frac(x, y)"
        x = (self.x).as_integer_ratio()
        return "Frac{}".format(x)

    # Py2.7 i Py3
    def __eq__(self, other):
        return self.x/self.y == other.x/other.y

    def __ne__(self, other):
        return self.x/self.y != other.x/other.y

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
        return other + self.x/self.y

    def __radd__(self, other):
        return self.x/self.y + other.x/other.y

    __radd__ = __add__              # int+frac

    def __sub__(self, other):
        return other - self.x/self.y

    def __rsub__(self, other):
        return other.x/other.y - self.x/self.y

    __rsub__ = __sub__              # int-frac

    def __mul__(self, other):   # frac1*frac2, frac*int
        return self.x/self.y * other

    def __rmul__(self, other):   # frac1*frac2, frac*int
        return self.x/self.y * other.x/other.y

    __rmul__ = __mul__              # int*frac

    """
    def __div__(self, other):  # frac1/frac2, frac/int, Py2
        return (self.x/self.y) / other

    def __rdiv__(self, other):  # int/frac, Python 2
        return self.x/self.y * other.y/other.x

     __rdiv__ = __div__
    """

    def __truediv__(self, other):  # frac1/frac2, frac/int, Py3
        return other / (self.x/self.y)

    def __rtruediv__(self, other):  # int/frac, Py3
        return self.x/self.y * other.y/other.x

    __rtruediv__ = __truediv__
    # operatory jednoargumentowe

    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):         # -frac = (-1)*frac
        return (-1) * self.x/self.y

    def __invert__(self):      # odwrotnosc: ~frac
        return self.y/self.x

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
        self.assertEqual(repr(self.f4), "Frac(1, 4)")

    def test_cmp(self):
        self.assertTrue(Frac(1, 1) == Frac(1, 1))
        self.assertFalse(Frac(0.25) != Frac(0.25))
        self.assertTrue(Frac(2, 2) > Frac(1, 2))

    def test_add(self):
        self.assertEqual(2 + Frac(1, 2), 2.5)
        self.assertEqual(Frac(0.25) + Frac(0.25), 0.5)
        self.assertEqual(Frac(5, 5) + Frac(1, 5), 1.2)

    def test_sub(self):
        self.assertEqual(3 - Frac(2, 2), 2)
        self.assertEqual(Frac(0.25) - Frac(0.25), 0)

    def test_mul(self):
        self.assertEqual(3 * Frac(2, 2), 3)
        self.assertEqual(Frac(0.25) * Frac(0.25), 0.0625)

    def test_div(self):
        self.assertEqual(3 / Frac(2, 2), 3)
        self.assertEqual(Frac(0.25) / Frac(0.25), 1)

    def test_invert(self):
        self.assertEqual(~Frac(2), 0.5)


if __name__ == "__main__":
    unittest.main()     # wszystkie testy
