"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 패션왕 신해빈
description : 조합
"""

from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    clothes = defaultdict(list)

    for _ in range(n):
        A, B = map(str, input().split())
        clothes[B].append(A)

    result = 1

    for values in clothes.values():
        result *= len(values) + 1

    print(result - 1)
