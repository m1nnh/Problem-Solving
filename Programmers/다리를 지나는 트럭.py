"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 다리를 지나는 트럭
description : 큐, 스택
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    queue = deque()
    stack = []
    length = len(truck_weights)
    truck_weights = truck_weights[::-1]
    queue.append([1, truck_weights.pop()])
    while len(stack) != length:
        if truck_weights:
            next_weight = truck_weights.pop()
            len_queue = len(queue)
            sum_value = 0
            for i in range(len_queue):
                now_time, now_weight = queue.popleft()
                if now_time + 1 <= bridge_length:
                    queue.append([now_time + 1, now_weight])
                    sum_value += now_weight
                else:
                    stack.append(now_weight)
            if sum_value + next_weight <= weight:
                queue.append([1, next_weight])
            else:
                truck_weights.append(next_weight)
        else:
            len_queue = len(queue)
            for i in range(len_queue):
                now_time, now_weight = queue.popleft()
                if now_time + 1 <= bridge_length:
                    queue.append([now_time + 1, now_weight])
                else:
                    stack.append(now_weight)

        answer += 1

    return answer
