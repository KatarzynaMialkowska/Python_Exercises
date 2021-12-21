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
        move = random.randint(0, self.size())
        iter = self.head
        for x in range(0, move-1):
            print("move" + move-1)
            iter = iter.next

        iter.prev.next = iter.next
        iter.next.prev = iter.prev
        iter.data = 0

    def get(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def first(self):
        return self.head.data

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def is_empty(self):
        return self.head is None

    def is_full(self):   # nigdy nie jest pusta
        return False

    def clear(self):
        self.head = self.tail = None

    def view(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="-")
            temp = temp.next


if __name__ == '__main__':

    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)

    queue.view()
    queue.remove()
    print("empty: ", queue.is_empty())
    queue.view()
    queue.clear()
    print("empty:", queue.is_empty())
