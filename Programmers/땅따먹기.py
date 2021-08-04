"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 땅따먹기
description : 다이나믹 프로그래밍
"""


def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    answer = max(land[-1])
    return answer
