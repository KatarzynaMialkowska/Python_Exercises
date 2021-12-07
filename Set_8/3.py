import random


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    random.seed()
    k = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if pow(x, 2) + pow(y, 2) <= 1:
            k = k + 1
    pi = 4 * k / n
    return pi


print("pi =", calc_pi(100000))
