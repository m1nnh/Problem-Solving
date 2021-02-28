"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 1로 만들기
description : 다이나믹 프로그래밍
"""

N = int(input())
D = [0] * (int(1e6) + 1)

for i in range(2, N + 1):
    D[i] = D[i - 1] + 1
    if i % 2 == 0:
        D[i] = min(D[i], D[i // 2] + 1)
    if i % 3 == 0:
        D[i] = min(D[i], D[i // 3] + 1)
print(D[N])
