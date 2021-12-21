import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def insert(self, val):
        if self.tail is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def remove(self):   # zwraca losowy element
        move = random.randint(1, self.size())
        iter = self.head
        print("aaaaaa")
        print(move)
        if move == 1:
            return self.get()
        elif move == self.size():
            result = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            return result
        else:
            for x in range(1, move):
                iter = iter.next
            result = iter.data
            iter.prev.next = iter.next
            iter.next.prev = iter.prev
            return result

    def get(self):
        if self.head is None:
            return None
        else:
            iter = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return iter

    def first(self):
        return self.head.data

    def size(self):
        iter = self.head
        count = 0
        while iter is not None:
            count = count + 1
            iter = iter.next
        return count

    def is_empty(self):
        return self.head is None

    def is_full(self):   # nigdy nie jest pusta
        return False

    def clear(self):
        self.head = self.tail = None

    def view(self):
        iter = self.head
        while iter is not None:
            print(iter.data, end="-")
            iter = iter.next


if __name__ == '__main__':

    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)

    queue.view()
    print(f"remove: {queue.remove()}")
    print(f"empty: {queue.is_empty()}")
    queue.view()
    queue.clear()
    print(f"\nempty: {queue.is_empty()}")
