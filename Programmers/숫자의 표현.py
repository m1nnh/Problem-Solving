"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 숫자의 표현
description : 수학
"""


def solution(n):
    answer = 1
    for i in range(1, n):
        result = i
        for j in range(i + 1, n + 1):
            result += j
            if result >= n:
                break
        if result == n:
            answer += 1
    return answer
