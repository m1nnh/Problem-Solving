"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 절대값 힙
description : 힙
"""

import sys
import heapq

input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    x = int(input())
    if x != 0:
        if x < 0:
            heapq.heappush(queue, (-x, 'minus'))
        else:
            heapq.heappush(queue, (x, 'plus'))
    else:
        if queue:
            value, status = heapq.heappop(queue)
            print(value if status == 'plus' else -value)
        else:
            print(0)
