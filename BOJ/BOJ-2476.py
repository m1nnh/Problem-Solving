"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 주사위 게임
description : 수학
"""

n = int(input())

grade = []

for i in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        grade.append(10000 + a * 1000)
    elif a == b:
        grade.append(1000 + a * 100)
    elif a == c:
        grade.append(1000 + a * 100)
    elif b == c:
        grade.append(1000 + b * 100)
    else:
        grade.append(max(a, b, c) * 100)
print(max(grade))
