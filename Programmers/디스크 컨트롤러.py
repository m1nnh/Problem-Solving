"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 디스크 컨트롤러
description : 힙
"""

import heapq


def solution(jobs):
    times = []
    time = 0
    start = -1
    queue = []

    while len(times) != len(jobs):
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(queue, (job[1], job[0]))
        if len(queue) != 0:
            start = time
            cpu_burst_time, input_time = heapq.heappop(queue)
            time += cpu_burst_time
            times.append(abs(start - input_time) + cpu_burst_time)
        else:
            time += 1
    answer = sum(times) // len(times)
    return answer
