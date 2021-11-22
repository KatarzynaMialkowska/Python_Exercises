import unittest
import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):         # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):    # obsługa point1 == point2
        return (self.x == other.x and self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return (self.x != other.x)

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(self.x*self.x + self.y*self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1, 1)
        self.p2 = Point(2, 2)

    def test_print(self):      # test str() i repr()
        self.assertEqual(str(self.p1), "(1, 1)")
        self.assertEqual(str(self.p2), "(2, 2)")
        self.assertEqual(repr(self.p1), "Point(1, 1)")
        self.assertEqual(repr(self.p2), "Point(2, 2)")

    def test_cmp(self):
        self.assertTrue(Point(1, 1) == Point(1, 1))
        self.assertFalse(Point(1, 1) == Point(1, 2))
        self.assertTrue(Point(2, 2) != Point(1, 1))
        self.assertFalse(Point(0, 0) != Point(0, 0))

    def test_add(self):
        self.assertEqual(Point(0, 0) + Point(1, 1), Point(1, 1))
        self.assertEqual(Point(2, 2) + Point(1, 1), Point(3, 3))
        self.assertEqual(Point(5, 5) + Point(5, 5), Point(10, 10))
        self.assertEqual(Point(-5, -20) + Point(5, 5), Point(0, -15))

    def test_sub(self):
        self.assertEqual(Point(0, 0) - Point(1, 1), Point(-1, -1))
        self.assertEqual(Point(2, 2) - Point(1, 1), Point(1, 1))
        self.assertEqual(Point(5, 5) - Point(5, 5), Point(0, 0))
        self.assertEqual(Point(-5, -20) - Point(5, 5), Point(-10, -25))

    def test_mul(self):
        self.assertEqual(Point(0, 0) * Point(1, 1), 0)
        self.assertEqual(Point(2, 2) * Point(1, 1), 4)
        self.assertEqual(Point(5, 5) * Point(5, 5), 50)
        self.assertEqual(Point(-5, -20) * Point(5, 5), -125)

    def test_cross(self):
        self.assertEqual(self.p1.cross(Point(0, 0)), 0)
        self.assertEqual(self.p1.cross(Point(10, 15)), 5)
        self.assertEqual(self.p2.cross(Point(-2, 0)), 4)
        self.assertEqual(self.p2.cross(Point(-4, 35)), 78)

    def test_length(self):
        self.assertEqual(self.p1.length(), 1.4142135623730951)
        self.assertEqual(self.p2.length(), 2.8284271247461903)

    def test_hash(self):
        self.assertEqual(hash(Point(1, 1)), hash((1, 1)))
        self.assertEqual(hash(Point(2, 2)), hash((2, 2)))


if __name__ == "__main__":
    unittest.main()     # wszystkie testy
