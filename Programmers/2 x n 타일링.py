"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 2 x n 타일링
description : 다이나믹 프로그래밍
"""


def solution(n):
    dp = [0] * (60001)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000007

    answer = dp[n]
    return answer
