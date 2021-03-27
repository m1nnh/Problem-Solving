"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 제곱 ㄴㄴ수
description : 에라토스테네스의 체
"""

import math
import sys

input = sys.stdin.readline

min_value, max_value = map(int, input().split())
count = max_value - min_value + 1
visited = [True] * count

for i in range(2, int(math.sqrt(max_value)) + 1):
    if i ** 2 > max_value:
        break
    else:
        div = min_value // (i ** 2)
        if div == 0:
            div += 1

        for j in range(div * (i ** 2), max_value + 1, i ** 2):
            if j < min_value:
                continue
            else:
                if visited[j - min_value] is True:
                    visited[j - min_value] = False
                    count -= 1
print(count)
