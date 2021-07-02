"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 예산
description : 정렬
"""


def solution(d, budget):
    answer = 0
    d.sort()

    for i in d:
        if budget - i >= 0:
            answer += 1
            budget -= i
        else:
            break
    return answer
