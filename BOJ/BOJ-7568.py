"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 덩치
description : 구현, 브루트포스 알고리즘
"""

N = int(input())
P = []
count = 0
Rank = []
for i in range(N):
    A = list(map(int, input().split()))
    P.append(A)

for i in range(N):
    count = 0
    for j in range(N):
        if P[i][0] < P[j][0]:
            if P[i][1] < P[j][1]:
                count += 1
    Rank.append(count + 1)

[print(x, end=' ') for x in Rank]
