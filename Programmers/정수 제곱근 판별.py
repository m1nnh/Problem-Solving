"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 정수 제곱근 판별
description : 수학
"""

import math


def solution(n):
    answer = 0
    if int(math.sqrt(n)) ** 2 == n:
        answer = (int(math.sqrt(n)) + 1) ** 2
    else:
        answer = -1

    return answer
