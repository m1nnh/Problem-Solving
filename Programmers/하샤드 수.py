"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 하샤드 수
description : 수학
"""


def solution(x):
    answer = True
    array_x = list(map(int, str(x)))

    if x % sum(array_x) != 0:
        answer = False
    return answer
