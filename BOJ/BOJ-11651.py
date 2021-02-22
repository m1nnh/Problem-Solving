"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 좌표 정렬하기 2
description : 정렬
"""

N = int(input())

Coord = []

for i in range(N):
    A = list(map(int, input().split()))
    Coord.append(A)

Coord.sort(key=lambda x: (x[1], x[0]))

[print(*x) for x in Coord]
