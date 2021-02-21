import math

M, N = map(int, input().split())
check = [True] * (N + 1)
check[0], check[1] = False, False

for i in range(2, int(math.sqrt(N)) + 1):
    if check[i] is True:
        for j in range(i * 2, N + 1, i):
            check[j] = False

for i in range(M, N):
    if check[i] is True:
        print(i, end=' ')
