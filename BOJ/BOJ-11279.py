"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최대 힙
description : 힙
"""

import heapq
import sys

input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    x = int(input())

    if x != 0:
        heapq.heappush(queue, -x)
    else:
        if queue:
            print(-heapq.heappop(queue))
        else:
            print(0)
