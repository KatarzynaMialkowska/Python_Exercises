import unittest
from points import Point
import math


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):        # "Circle(x, y, radius)"
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return math.pi*self.radius*self.radius

    def move(self, x, y):      # przesuniecie o (x, y)
        self.pt.x = self.pt.x + x
        self.pt.y = self.pt.y + y
        return self

    def cover(self, other):   # najmniejszy okrąg pokrywający oba
        distSq = math.sqrt(pow((self.pt.x - other.pt.x), 2) +
                           pow((self.pt.y - other.pt.y), 2))
        if (distSq + other.radius <= self.radius):
            return self if (self.area() > other.area()) else other
        else:
            return Circle((self.pt.x + other.pt.x)/2, (self.pt.y + other.pt.y)/2, (distSq+self.radius+other.radius)/2)

# Kod testujący moduł.


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(1, 1, 1)
        self.c2 = Circle(0, 0, 1)
        self.c3 = Circle(1, 1, 0)

    def test_print(self):
        self.assertEqual(str(self.c1), "Circle(1, 1, 1)")
        self.assertEqual(str(self.c2), "Circle(0, 0, 1)")

    def test_cmp(self):
        self.assertFalse(self.c1 == self.c2)
        self.assertTrue(self.c1 != self.c2)

    def test_area(self):
        self.assertEqual(self.c1.area(), 3.141592653589793)
        self.assertEqual(self.c2.area(), 3.141592653589793)

    def test_move(self):
        self.assertEqual(self.c2.move(1, 1), self.c1)
        self.assertEqual(self.c2.area(), 3.141592653589793)

    def test_cover(self):
        self.assertEqual(self.c2.cover(Circle(0, 0, 0.5)), self.c2)
        self.assertEqual(self.c2.cover(Circle(2, 2, 1)),
                         Circle(1, 1, 2.414213562373095))


if __name__ == "__main__":
    unittest.main()     # wszystkie testy
