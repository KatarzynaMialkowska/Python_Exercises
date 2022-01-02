from math import sqrt
import random


def randomA(num, n):
    if num <= 0 or n <= 0 or not isinstance(num, int):
        raise ValueError("bad value")
    list = []
    for i in range(num):
        list.append(random.randint(0, n-1))

    return list


# co dziesiate liczby sa losowane z wyliczonego przedzialu rosnacego
def randomB(num, n):
    if num <= 0 or n <= 0 or not isinstance(num, int):
        raise ValueError("bad value")
    list = []
    if n <= 10:
        s = 0
        e = n
        scale = 0
    else:
        s = 0
        e = 11
        scale = n / 10
    while (num > 0):
        list.append(random.randint(s, e-1))
        if(num % 10 == 0):
            if e > 10:
                if(e+scale < n):
                    s = e
                    e = int(e + scale)
                else:
                    s = e
                    e = n
                if(s == e):
                    s = s - scale
                if(s < 0):
                    s = 0
        num = num - 1

    return list

# w odwrodten kolejnosci: co dziesiate liczby sa losowane z wyliczonego przedzialu rosnacego


def randomC(num, n):
    if num <= 0 or n <= 0 or not isinstance(num, int):
        raise ValueError("bad value")
    list = []
    if n <= 10:
        s = 0
        e = n
        scale = 0
    else:
        s = 0
        e = 11
        scale = n / 10
    while (num > 0):
        list.insert(0, (random.randint(s, e-1)))
        if(num % 10 == 0):
            if e > 10:
                if(e+scale < n):
                    s = e
                    e = int(e + scale)
                else:
                    s = e
                    e = n
                if(s == e):
                    s = s - scale
                if(s < 0):
                    s = 0
        num = num - 1

    return list


def randomD(num, n):
    if num <= 0 or n <= 0 or not isinstance(num, int):
        raise ValueError("bad value")
    list = []
    for i in range(num):
        list.append(float(random.gauss(0, n)))

    return list


def randomE(num, n):
    if num <= 0 or n <= 0 or not isinstance(num, int) or not isinstance(n, int):
        raise ValueError("bad value")

    k = int(sqrt(num))
    if pow(k, 2) != num:
        raise ValueError("error")

    list = []
    for i in range(num):
        list.append(random.randint(0, k))

    return list
