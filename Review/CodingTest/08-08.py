"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 효율적인 화폐 구성
description : 다이나믹 프로그래밍

"""

N, M = map(int, input().split())
Coin = []
dp = [10001] * (M + 1)
dp[0] = 0

for i in range(N):
    Coin.append(int(input()))

for i in range(N):
    for j in range(Coin[i], M + 1):
        if dp[j - Coin[i]] != 10001:
            dp[j] = min(dp[j], dp[j - Coin[i]] + 1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
