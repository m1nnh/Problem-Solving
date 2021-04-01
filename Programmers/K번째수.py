"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : K번째
description : 정렬
"""


def solution(array, commands):
    answer = []
    [answer.append(sorted(array[start - 1: end])[index - 1]) for start, end, index in commands]

    return answer
