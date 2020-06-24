"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 주사위 게임
description : 수학, 구현, 사칙연산
"""

n = int(input())

c, s = 100, 100

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        s -= a
    elif b > a:
        c -= b
    else:
        continue

print(c)
print(s)
