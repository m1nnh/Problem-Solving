"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 거스름돈
description : DP
"""


def solution(n, money):
    answer = [0] * (n + 1)
    answer[0] = 1
    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                answer[price] += answer[price - coin]

    return answer[-1] % 1000000007
