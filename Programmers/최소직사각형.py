"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최소직사각형
description : 수학
"""


def solution(sizes):
    max_value = []
    min_value = []

    for i in range(len(sizes)):
        if sizes[i][0] == sizes[i][1]:
            max_value.append(sizes[i][0])
            min_value.append(sizes[i][1])
        else:
            max_value.append(max(sizes[i]))
            min_value.append(min(sizes[i]))

    answer = max(max_value) * max(min_value)

    return answer
