"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 볼링공 고르기
description : 그리디
"""

from itertools import combinations

N, M = map(int, input().split())
K = list(map(int, input().split()))
cmb = combinations(K, 2)
result = 0
for i, j in list(cmb):
    if i == j:
        continue
    result += 1

print(result)
