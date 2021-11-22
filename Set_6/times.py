class Time:
    """Klasa reprezentująca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancję klasy Time."""
        if s < 0:
            raise ValueError("ujemny czas")
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcinków czasu."""
        return Time(self.s + other.s)
    
    def __sub__(self, other):
        """Odejmowanie odcinków czasu."""
        return Time(self.s - other.s)

    #def __cmp__(self, other): # Py2, porównywanie, -1|0|+1
    #    """Porównywanie odcinków czasu."""
        if ((self - other) == 0 ): return 0
        if ((self - other) > 0 ): return 1
        else: return -1

    # Py2.7 i Py3, rich comparisons.
    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __lt__(self, other):
        return self.s < other.s

    def __le__(self, other):
        return self.s <= other.s

    # nadmiarowe
    def __gt__(self, other):
        return self.s > other.s

    # nadmiarowe
    def __ge__(self, other):
        return self.s >= other.s

    def __int__(self):                  # int(time1) 
        """Konwersja odcinka czasu do int."""
        return self.s

# Kod testujący moduł - dopisać co najmniej dwa testy do każdej sekcji.

import unittest

class TestTime(unittest.TestCase):

    def setUp(self):
        self.t1 = Time(3723)
        self.t2 = Time(3600)

    def test_print(self):      # test str() i repr()
        self.assertEqual(str(self.t1), "01:02:03")
        self.assertEqual(repr(self.t1), "Time(3723)")
        self.assertEqual(str(self.t2), "01:00:00")
        self.assertEqual(repr(self.t2), "Time(3600)")

    def test_cmp(self):
        # Trzeba sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time(2) == Time(2))
        self.assertFalse(Time(2) == Time(3))
        self.assertTrue(Time(2) != Time(3))
        self.assertFalse(Time(2) != Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertFalse(Time(4) < Time(3))
        self.assertTrue(Time(2) <= Time(3))
        self.assertFalse(Time(4) <= Time(3))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertFalse(Time(2) >= Time(3))
        self.assertTrue(Time(10) >= Time(3))
        self.assertTrue(Time(10) == Time(10))

    def test_add(self):   # musi działać porównywanie
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(5) + Time(5), Time(10))
        self.assertEqual(Time(3) - Time(3), Time(0))

    def test_int(self): 
        self.assertEqual(int(Time(3600.34)), 3600)
        self.assertEqual(int(Time(2413)), 2413)
        
    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy