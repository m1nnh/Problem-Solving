"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 이항 계수 1
description :
"""

from itertools import combinations

N, K = map(int, input().split())

arr = [x for x in range(N)]

result = list(combinations(arr, K))
print(len(result))
