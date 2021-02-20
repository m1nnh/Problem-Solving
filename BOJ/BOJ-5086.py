"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 배수와 약
description : 수학, 구현
"""

a, b = map(int, input().split())

while a != 0 and b != 0:
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')
    a, b = map(int, input().split())
