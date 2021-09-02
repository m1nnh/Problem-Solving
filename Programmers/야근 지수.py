"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 야근 지수
description : 힙
"""

import heapq


def solution(n, works):
    answer = 0
    queue = []

    for i in works:
        heapq.heappush(queue, -i)

    while n != 0 and queue:
        now_work = heapq.heappop(queue)

        now_work += 1
        n -= 1

        if now_work == 0:
            continue
        else:
            heapq.heappush(queue, now_work)

    if queue:
        for i in queue:
            answer += i ** 2

    return answer
