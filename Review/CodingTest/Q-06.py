"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 무지의 먹방 라이브
description : 그리디
"""

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    eat, previous = 0, 0
    length = len(food_times)

    while True:
        if eat + ((q[0][0] - previous) * length) > k:
            break

        now = heapq.heappop(q)[0]
        eat += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - eat) % length][1]
