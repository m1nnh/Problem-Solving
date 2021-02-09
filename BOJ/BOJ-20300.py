"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 서강근육맨
description : Greedy
"""

N = int(input())
T = list(map(int, input().split()))
M = 0
T.sort()

if len(T) % 2 == 0:
    for i in range(N // 2):
        M = max(M, T[i] + T[N - 1 - i])
else:
    for i in range(N // 2):
        M = max(M, T[i] + T[N - 2 - i])
    M = max(M, T[-1])
print(M)
