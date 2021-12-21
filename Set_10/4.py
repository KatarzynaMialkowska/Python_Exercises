import unittest


class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):   # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):   # nigdy nie jest pusta
        return False

    def put(self, data):
        if self.is_full():
            raise ValueError("przepelniona kolejka")
        self.items.append(data)

    def get(self):
        if self.is_empty():
            raise ValueError("pusta kolejka")
        return self.items.pop(0)   # mało wydajne!


class TestQueue(unittest.TestCase):
    def test_put(self):
        q1 = Queue()

        for item in ["a", 2, 3.5]:
            q1.put(item)

        self.assertEqual(q1.is_full(), 0)
        self.assertEqual(q1.get(), "a")
        self.assertEqual(q1.get(), 2)
        self.assertEqual(q1.get(), 3.5)

    def test_get(self):
        q1 = Queue()
        for item in ["a", 2, 3.5]:
            q1.put(item)
        self.assertEqual(q1.get(), "a")
        self.assertEqual(q1.get(), 2)
        self.assertEqual(q1.get(), 3.5)
        self.assertEqual(q1.is_empty(), 1)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
