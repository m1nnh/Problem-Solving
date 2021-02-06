"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최소 힙
description : 우선순위 큐, 자료구조
"""

import heapq
import sys

input = sys.stdin.readline
N = int(input())
queue = []

for i in range(N):
    x = int(input())
    if x == 0:
        if queue:
            print(heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, x)
