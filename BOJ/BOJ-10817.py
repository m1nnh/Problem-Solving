"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Three number
description : Math
"""

a, b, c = map(int, input().split())

if a >= b and a >= c:
    if b >= c:
        print(b)
    else:
        print(c)
elif b >= a and b >= c:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= a:
        print(b)
    else:
        print(a)
