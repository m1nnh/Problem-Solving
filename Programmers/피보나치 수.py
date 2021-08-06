"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 피보나치 수
description : 다이나믹 프로그래밍
"""


def solution(n):
    dp = [0 for _ in range(100001)]
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    answer = dp[n] % 1234567

    return answer
