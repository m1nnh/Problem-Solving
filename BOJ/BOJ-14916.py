"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 거스름돈
description : Greedy
"""

N = int(input())
dp = [int(1e9)] * 100001
dp[2] = 1
dp[5] = 1

for i in range(6, N + 1):
    dp[i] = min(dp[i - 2] + 1, dp[i - 5] + 1)
if dp[N] >= int(1e9):
    print(-1)
else:
    print(dp[N])
