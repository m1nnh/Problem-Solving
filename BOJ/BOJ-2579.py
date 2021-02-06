"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 계단 오르기
description : 다이나믹 프로그래밍
"""

N = int(input())
Stairs = []
dp = [0] * N

for _ in range(N):
    Stairs.append(int(input()))

dp[0] = Stairs[0]
dp[1] = max(dp[0] + Stairs[1], Stairs[1])
dp[2] = max(dp[0] + Stairs[2], Stairs[1] + Stairs[2])

for i in range(3, N):
    dp[i] = max(dp[i - 2] + Stairs[i], dp[i - 3] + Stairs[i - 1] + Stairs[i])

print(dp[-1])
