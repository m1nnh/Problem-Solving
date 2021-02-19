"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 상하좌우
description : 구현
"""

N = int(input())
Array = input().split()
Move = ['L', 'R', 'U', 'D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x, y = 1, 1
nx, ny = 0, 0
for i in Array:
    for j in range(4):
        if i == Move[j]:
            nx = dx[j] + x
            ny = dy[j] + y
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    else:
        x, y = nx, ny
print(y, x)
