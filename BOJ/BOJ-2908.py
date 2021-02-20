"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Constants
description : Implementation
"""

a, b = map(str, input().split())

a = a[::-1]
b = b[::-1]

if int(a) > int(b):
    print(a)
else:
    print(b)
