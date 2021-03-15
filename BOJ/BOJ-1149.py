"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : RGB 거리
description : 다이나믹 프로그래밍
"""

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1] + dp[i][0], dp[i - 1][2] + dp[i][0])
    dp[i][1] = min(dp[i - 1][0] + dp[i][1], dp[i - 1][2] + dp[i][1])
    dp[i][2] = min(dp[i - 1][0] + dp[i][2], dp[i - 1][1] + dp[i][2])

print(min(dp[-1]))
