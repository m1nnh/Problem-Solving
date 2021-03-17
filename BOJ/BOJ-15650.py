"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : N과 M(2)
description : 순열과 조합
"""

from itertools import combinations

N, M = map(int, input().split())
array = [x for x in range(1, N + 1)]

comb = list(combinations(array, M))

for i in comb:
    for j in i:
        print(j, end=' ')
    print()
