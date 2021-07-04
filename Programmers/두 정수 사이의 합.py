"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 두 정수 사이의 합
description : 수학
"""


def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a, b + 1):
            answer += i
    elif b < a:
        for i in range(b, a + 1):
            answer += i
    else:
        answer = a
    return answer
