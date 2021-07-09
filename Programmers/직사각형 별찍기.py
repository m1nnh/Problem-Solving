"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 직사각형 별찍기
description : 구현
"""

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*" * a)
