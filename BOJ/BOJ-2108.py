"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 통계학
description : 구현, 정렬
"""

from collections import Counter
import sys

n = int(sys.stdin.readline())

num_list = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    avg, center, frq = num_list[0], num_list[0], num_list[0]
    rng = 0
else:
    avg = round(sum(num_list) / n)
    sorted_list = sorted(num_list)
    center = sorted_list[len(sorted_list) // 2]

    count_list = Counter(num_list)
    count_list = count_list.most_common()
    sort_list = sorted(count_list, key=lambda x: (-x[1], x[0]))
    print(sort_list)
    if sort_list[0][1] == sort_list[1][1]:
        frq = sort_list[1][0]
    else:
        frq = sort_list[0][0]
    rng = max(num_list) - min(num_list)
print(avg, center, frq, rng, sep='\n')
