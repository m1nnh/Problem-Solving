"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 소수 찾기2
description : 조합
"""

from itertools import permutations

import math


def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    dic = {}

    for i in range(1, len(numbers) + 1):
        comb_numbers = list(permutations(numbers, i))
        for j in comb_numbers:
            string = ""
            for k in j:
                string += k
            num = int(string)
            if num not in dic:
                dic[num] = 1
                if prime_check(num) is True:
                    answer += 1

    return answer


def prime_check(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
        if count > 2:
            return False
    if count == 2:
        return True
    else:
        return False
