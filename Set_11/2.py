import generate
import os
import unittest


def insertsort(L, left, right):
    for i in range(right, left, -1):
        if L[i-1] > L[i]:
            L[i-1], L[i] = L[i], L[i-1]
    for i in range(left+2, right+1):
        j = i
        item = L[i]
        while item < L[j-1]:
            L[j] = L[j-1]
            j = j-1
        L[j] = item
    return L


def saveUnsortToFile(list):
    f = open("notSort.dat", "w")
    f.truncate(0)
    for i in range(len(list)):
        f.write(f"{i}\t{list[i]}\n")


def saveSortToFile(list):
    f = open("sort.dat", "w")
    f.truncate(0)
    for i in range(len(list)):
        f.write(f"{i}\t{list[i]}\n")


print("================")
L = generate.randomA(100, 100)
print(L)
saveUnsortToFile(L)
print(">>SORT<<")
print(insertsort(L, 0, 99))
saveSortToFile(insertsort(L, 0, 99))
os.system("gnuplot sortApdf.gnu")

print("================")
L = generate.randomB(100, 100)
print(L)
saveUnsortToFile(L)
print(">>SORT<<")
print(insertsort(L, 0, 99))
saveSortToFile(insertsort(L, 0, 99))
os.system("gnuplot sortBpdf.gnu")

print("================")
L = generate.randomC(100, 100)
print(L)
saveUnsortToFile(L)
print("SORT")
print(insertsort(L, 0, 99))
saveSortToFile(insertsort(L, 0, 99))
os.system("gnuplot sortCpdf.gnu")

print("================")
L = generate.randomD(100, 100)
print(L)
saveUnsortToFile(L)
print(">>SORT<<")
print(insertsort(L, 0, 99))
saveSortToFile(insertsort(L, 0, 99))
os.system("gnuplot sortDpdf.gnu")


class TestSort(unittest.TestCase):

    def test_sortA(self):
        list = generate.randomA(100, 100)
        sort = insertsort(list, 0, 99)
        list.sort()
        self.assertEqual(sort, list)

    def test_sortB(self):
        list = generate.randomB(100, 100)
        sort = insertsort(list, 0, 99)
        list.sort()
        self.assertEqual(sort, list)

    def test_sortC(self):
        list = generate.randomC(100, 100)
        sort = insertsort(list, 0, 99)
        list.sort()
        self.assertEqual(sort, list)

    def test_sortD(self):
        list = generate.randomD(100, 100)
        sort = insertsort(list, 0, 99)
        list.sort()
        self.assertEqual(sort, list)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
