"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최대공약수와 최소공배수
description : 수학
"""


def solution(n, m):
    answer = [GCD(n, m), (n * m) // GCD(n, m)]
    return answer


def GCD(n, m):
    max_value = max(n, m)
    min_value = min(n, m)

    temp = 0

    if max_value % min_value == 0 or max_value == min_value:
        return min_value
    while max_value % min_value != 0:
        temp = max_value % min_value
        max_value = min_value
        min_value = temp

    return temp
