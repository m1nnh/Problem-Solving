"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 줄 서는 방법
description : 수학
"""

import math


def solution(n, k):
    answer = []

    num_list = [i for i in range(1, n + 1)]

    while n != 0:
        temp = math.factorial(n - 1)
        idx, k = (k - 1) // temp, k % temp
        answer.append(num_list.pop(idx))
        n -= 1

    return answer
