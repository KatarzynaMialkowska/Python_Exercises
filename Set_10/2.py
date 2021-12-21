import unittest


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError("przepelniony stos")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("pusty stos")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data


class TestStack(unittest.TestCase):
    def test_push(self):
        s1 = Stack(3)
        for item in ["a", 2, 3.5]:
            s1.push(item)
        self.assertEqual(s1.is_full(), 1)
        self.assertEqual(s1.pop(), 3.5)
        self.assertEqual(s1.pop(), 2)
        self.assertEqual(s1.pop(), "a")

    def test_pop(self):
        s1 = Stack(3)
        for item in ["a", 2, 3.5]:
            s1.push(item)
        self.assertEqual(s1.pop(), 3.5)
        self.assertEqual(s1.pop(), 2)
        self.assertEqual(s1.pop(), "a")
        self.assertEqual(s1.is_empty(), 1)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
