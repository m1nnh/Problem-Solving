"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 주사위 세개
description : 수학, 사칙연
"""

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif a == c:
    print(1000 * a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(100 * max(a, b, c))


