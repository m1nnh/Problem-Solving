"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 이중우선순위큐
description : 이중우선순위큐
"""

import heapq


def solution(operations):
    answer = [0, 0]
    queue = []

    for i in range(len(operations)):
        op, number = operations[i].split()
        if op == "I":
            heapq.heappush(queue, int(number))
        elif op == "D":
            if queue:
                if number == "1":
                    max_index = queue.index(max(queue))
                    queue.pop(max_index)
                else:
                    heapq.heappop(queue)
            else:
                continue
    if len(queue) != 0:
        answer[0], answer[1] = max(queue), min(queue)

    return answer
