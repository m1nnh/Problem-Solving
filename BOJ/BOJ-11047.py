"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 블로그2
description : 그리디
"""

N, K = map(int, input().split())
Coin = []
count = 0

for i in range(N):
    Coin.append(int(input()))

while K != 0:
    result = K
    cnt = 0
    for i in Coin:
        if K // i >= 1:
            result = K
            cnt = K // i
            result = K - (i * cnt)
        else:
            break
    count += cnt
    K = result

print(count)
