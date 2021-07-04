"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 소수 찾기
description : 에라토스테네스 체
"""

import math


def solution(n):
    answer = prime_number(n)
    return answer


def prime_number(n):
    boolean_prime_number = [True] * (n + 1)
    boolean_prime_number[0], boolean_prime_number[1] = False, False

    for i in range(2, int(math.sqrt(n)) + 1):
        for j in range(i * 2, n + 1, i):
            boolean_prime_number[j] = False

    return boolean_prime_number.count(True)
