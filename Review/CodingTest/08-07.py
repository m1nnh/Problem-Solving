"""
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 바닥 공사
description : 다이나믹 프로그래밍

"""

N = int(input())
dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796

print(dp[N])
