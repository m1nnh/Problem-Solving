"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 내적
description : 수학
"""

def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer
