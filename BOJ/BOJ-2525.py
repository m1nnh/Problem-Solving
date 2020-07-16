"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : An oven clock
description : Math
"""

a, b = map(int, input().split())
c = int(input())
b += c
if b > 59:
    a = a + (b // 60)
    b = b % 60
    if a > 23:
        a -= 24
print('{} {}'.format(a, b))


