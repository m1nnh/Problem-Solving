"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : ATM
description : Greedy
"""

N = int(input())
Time = list(map(int, input().split()))
Time.sort()
dp = [0] * N
dp[0] = Time[0]

for i in range(1, N):
    dp[i] = dp[i - 1] + Time[i]

print(sum(dp))
