import time


def reP(i, j):
    if i == 0 and j == 0:
        return 0.5
    if i > 0 and j == 0:
        return 0.0
    if j > 0 and i == 0:
        return 1.0
    if j > 0 and i > 0:
        return 0.5*(reP(i-1, j)+reP(i, j-1))


def P(i, j):
    arr = [[0 for x in range(i+1)] for y in range(j+1)]
    for x in range(1, 1 + max(i, j)):
        arr[x][0] = 0
        arr[0][x] = 1
    for p in range(1, j + 1):
        for l in range(1, i + 1):
            arr[l][p] = 0.5*(arr[l-1][p] + arr[l][p-1])
            # print(arr[l][p])
    return arr[i][j]


start = time.time()
print(P(10, 10))
end = time.time()
print(f"time dyn: {end - start}")
print("======")
start = time.time()

print(reP(10, 10))
end = time.time()
print(f"time rec: {end - start}")
