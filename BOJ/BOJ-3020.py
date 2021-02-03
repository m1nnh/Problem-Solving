"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 개똥벌레
description : 부분합
"""

N, H = map(int, input().split())
Cave = [int(input()) for _ in range(N)]

A = [0] * (H + 2)
B = [0] * (H + 2)
result = [0] * (H + 2)


for i in range(N):
    h = Cave[i]
    if i % 2 == 0:
        B[h + 1] += 1
    else:
        A[H - h] += 1

for i in range(2, H + 1):
    B[i] += B[i - 1]

for i in range(H, -1, -1):
    A[i] += A[i + 1]


for i in range(1, H + 1):
    result[i] = A[i] + B[i]

print(N - max(result), result.count(max(result)))
