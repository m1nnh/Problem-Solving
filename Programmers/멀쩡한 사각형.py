"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 멀쩡한 사각형
description : 수학
"""

import math


def solution(w, h):
    answer = (w * h) - (w + h - math.gcd(w, h))
    return answer
