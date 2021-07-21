"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 위장
description : 해시, 수학
"""

from itertools import permutations


def solution(clothes):
    answer = 1
    dic = {}

    for ct, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1

    for value in dic.values():
        answer *= (value + 1)

    answer -= 1

    return answer
