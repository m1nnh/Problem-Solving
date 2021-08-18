"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 멀리 뛰기
description : DP
"""


def solution(n):
    answer = [0] * (n + 1)
    if n == 1:
        return 1
    answer[1], answer[2] = 1, 2

    for i in range(3, n + 1):
        answer[i] = answer[i - 1] + answer[i - 2]

    return answer[-1] % 1234567
