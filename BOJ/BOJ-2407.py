"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 조합
description : 재귀함수
"""

def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


N, M = map(int, input().split())
denominator = factorial(M) * factorial(N - M)
numerator = factorial(N)

print(numerator // denominator)
