"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 삼각 달팽이
description : 수학
"""


def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    number = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            res[x][y] = number
            number += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer
