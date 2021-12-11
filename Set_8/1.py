def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if b != 0:
        print(f"y = (-{a}x-{c})/{b}")
    if b == 0 and a != 0:
        print(f"x = -{c}/{a}")
    if a == 0 and b == 0:
        print("rownanie tozsamosciowe")
    if a == 0 and b != 0:
        print("rownanie sprzeczne")


solve1(1, 2, 3)
