"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 게임 개발
description : 구현
"""

N, M = map(int, input().split())
X, Y, D = map(int, input().split())
Array = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
result = 0
for i in range(N):
    Array.append(list(map(int, input().split())))

while True:
    if result == 4:
        X -= dx[D]
        Y -= dy[D]
        if Array[X][Y] == 1:
            break
        else:
            continue
    elif D == 0:
        D = 3
    else:
        D -= 1
    nx = dx[D] + X
    ny = dy[D] + Y

    if Array[nx][ny] == 0:
        X, Y = nx, ny
        result = 0
        count += 1
        Array[X][Y] = 1
    else:
        result += 1
print(count)
