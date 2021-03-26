"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 파도반 수열
description : 다이나믹 프로그래밍
"""

P = [0] * 101

P[1] = 1
P[2] = 1
P[3] = 1

for i in range(4, 101):
    P[i] = P[i - 2] + P[i - 3]

T = int(input())
for i in range(T):
    N = int(input())
    print(P[N])
