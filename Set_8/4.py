import math


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""

    if(a < 0 or b < 0 or c < 0):
        raise ValueError("cant be < 0")
    else:
        return math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))/4


try:
    print(heron(1, 1, 1))
    print(heron(1, 1, -1))
except ValueError:
    print("przechwycenie ValueError")
