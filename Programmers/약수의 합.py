"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 약수의 합
description : 수학
"""


def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer
