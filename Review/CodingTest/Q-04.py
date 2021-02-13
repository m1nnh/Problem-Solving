"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 만들 수 없는 금액
description : 그리디
"""

from itertools import combinations

N = int(input())
Coin = list(map(int, input().split()))
Check = [False] * 1000001
Check[0] = True

for i in Coin:
    Check[i] = True

for i in range(2, N + 1):
    cmb = combinations(Coin, i)
    for j in list(cmb):
        Check[sum(j)] = True

print(Check.index(False))
