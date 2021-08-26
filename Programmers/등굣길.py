"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 등굣길
description : 다이나믹 프로그래밍
"""


def solution(m, n, puddles):
    answer = [[0 for _ in range(m)] for _ in range(n)]
    answer[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if [j + 1, i + 1] in puddles:
                answer[i][j] = 0
            else:
                answer[i][j] = (answer[i - 1][j] + answer[i][j - 1]) % 1000000007

    return answer[-1][-1]
