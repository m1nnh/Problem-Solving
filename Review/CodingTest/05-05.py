"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 팩토리얼
description : 재귀함수
"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


N = int(input())

print(factorial(N))
