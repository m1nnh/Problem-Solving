"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최고의 집합
description : 수학
"""


def solution(n, s):
    answer = []

    if s < n:
        answer.append(-1)
    elif s % n == 0:
        answer = [s // n] * n
    else:
        answer = [s // n] * (n - (s % n)) + [(s // n) + 1] * (s % n)

    return answer
