"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 달팽이는 올라가고 싶다
description : 수학
"""

import sys

A, B, V = map(int, sys.stdin.readline().split())

count = (V - B) / (A - B)

if count == int(count):
    print(int(count))
else:
    print(int(count) + 1)
