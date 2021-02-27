"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 리모컨
description : 브루트포스 알고리즘
"""

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
broken = list(map(int, input().split()))
tmp = [x for x in range(10)]

channel = list(set(tmp) - set(broken))

result = abs(100 - N)
for i in range(1000000):
    flag = True
    for j in str(i):
        if int(j) not in channel:
            flag = False
            break

    if flag:
        result = min(result, len(str(i)) + abs(N - i))

print(result)
