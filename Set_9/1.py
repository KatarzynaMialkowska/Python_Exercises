class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __iter__(self):
        # Przy tworzeniu iteratora trzeba mieć zmiennć, która będzie pamiętać stan.
        # Przy kolejnym tworzeniu iteratora będzie ustawianie na początek.
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            node = self.current
            self.current = self.current.next
            return node.data
        else:   # self.current is None
            raise StopIteration

    next = __next__   # kompatybilność Py2 i Py3

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):          # klasy O(n)
        if self.is_empty():
            raise ValueError("pusta lista")
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            node = self.head
            while(node != self.tail):
                iter = node
                node = node.next
            iter.next = None
            self.tail = iter
            node = None
        self.length -= 1
        return self   # zwracamy usuwany node

    def join(self, other):
        if other.is_empty():
            raise ValueError("pusta lista")
        if other.head == other.tail:   # self.length == 1
            node = other.head
            self.insert_tail(Node(node))
            self.head = self.tail = None
        else:
            node = other.head
            while(node != other.tail):
                iter = node
                node = node.next
                self.insert_tail(Node(iter))
                other.remove_tail()
        return self

    def clear(self):     # czyszczenie listy
        if self.is_empty():
            raise ValueError("pusta lista")
        else:
            node = self.head
            while(node != self.tail):
                node = node.next
                self.remove_head()
            self.remove_head()


alist = SingleList()
alist.insert_head(Node(11))         # [11]
alist.insert_head(Node(22))         # [22, 11]
alist.insert_tail(Node(33))         # [22, 11, 33]
print("length {}".format(alist.length))  # odczyt atrybutu
print("length {}".format(alist.count()))  # wykorzystujemy interfejs
while not alist.is_empty():   # kolejność 22, 11, 33
    print("remove head {}".format(alist.remove_head()))

    # Zastosowanie.
alist = SingleList()
alist.insert_head(Node(11))         # [11]
alist.insert_head(Node(22))         # [22, 11]
alist.insert_tail(Node(33))         # [22, 11, 33]


for item in alist:   # kolejność 22, 11, 33
    print(item)
alist.remove_head()         # [11, 33]
print("============")

for item in alist:   # kolejność 22, 11, 33
    print(item)
print("============")
alistTest = SingleList()
alistTest.insert_head(Node(11))         # [11]
alistTest.insert_head(Node(22))         # [22, 11]
alistTest.insert_tail(Node(33))         # [22, 11, 33]
alistTest.insert_tail(Node(44))         # [22, 11, 33, 44]

for item in alistTest:   # kolejność 22, 11, 33
    print(item)


alistTest.remove_tail()         # [22, 11, 33]
alistTest.remove_tail()         # [22, 11, 33]

print("============")
for item in alistTest:   # kolejność 22, 11, 33
    print(item)

elo = alist.join(alistTest)
print("======join======")
for item in alistTest:   # kolejność 22, 11, 33
    print(item)
print("============")

for item in elo:   # kolejność 22, 11, 33
    print(item)

elo.clear()

print("======clear======")

for item in elo:   # kolejność 22, 11, 33
    print(item)
