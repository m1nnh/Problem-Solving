"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 종이의 개수
description : 분할정복, 재귀
"""


def recursive(n, x, y):
    start = array[y][x]

    if n == 0:
        return

    flag = True

    for i in range(y, y + n):
        if not flag:
            break
        for j in range(x, x + n):
            if array[i][j] != start:
                recursive(n // 3, x, y)
                recursive(n // 3, x + n // 3, y)
                recursive(n // 3, x + 2 * n // 3, y)
                recursive(n // 3, x, y + n // 3)
                recursive(n // 3, x, y + 2 * n // 3)
                recursive(n // 3, x + n // 3, y + n // 3)
                recursive(n // 3, x + 2 * n // 3, y + n // 3)
                recursive(n // 3, x + n // 3, y + 2 * n // 3)
                recursive(n // 3, x + 2 * n // 3, y + 2 * n // 3)
                flag = False
                break

    if flag:
        if start == -1:
            count[-1] += 1
        elif start == 0:
            count[0] += 1
        else:
            count[1] += 1


N = int(input())
array = []
count = [0] * 3

for i in range(N):
    array.append(list(map(int, input().split())))
recursive(N, 0, 0)
print(count[-1])
print(count[0])
print(count[1])
