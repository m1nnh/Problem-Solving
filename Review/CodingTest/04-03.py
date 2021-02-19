"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 왕실의 나이트
description : 구현
"""

N = input()
x = int(N[1])
y = int(ord(N[0])) - int(ord('a')) + 1
count = 0

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

for i, j in steps:
    dx = x + i
    dy = y + j
    if dx < 1 or dy < 1 or dx > 8 or dy > 8:
        continue
    else:
        count += 1
print(count)
