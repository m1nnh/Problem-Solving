"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 2 * n 타일링
description : 다이나믹 프로그래밍
"""

N = int(input())
dp = [0] * (N + 1)
dp[1] = 1
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 10007
print(dp[N])
