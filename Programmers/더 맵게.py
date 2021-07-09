"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 더 맵게
description : 힙
"""

import heapq


def solution(scoville, K):
    answer = 0
    queue = []

    for i in scoville:
        heapq.heappush(queue, i)

    while len(queue) > 1:
        min1 = heapq.heappop(queue)
        if min1 >= K:
            break
        min2 = heapq.heappop(queue)

        heapq.heappush(queue, min1 + (min2 * 2))
        answer += 1

    if len(queue) == 1 and sum(queue) < K:
        answer = -1
    return answer
