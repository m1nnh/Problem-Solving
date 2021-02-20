"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 크냐?
description : 수학, 구현, 사칙연산
"""

a, b = map(int, input().split())

while a != 0 and b != 0:
    if a > b:
        print("Yes")
    else:
        print("No")
    a, b = map(int, input().split())
