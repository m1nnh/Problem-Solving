"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 행복 유치원
description : Greedy
"""

N, K = map(int, input().split())
Tail = list(map(int, input().split()))
dp = []

for i in range(N - 1):
    dp.append(Tail[i + 1] - Tail[i])
dp.sort()
print(sum(dp[:N - K]))
