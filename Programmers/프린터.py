"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 프린터
description : 큐
"""

from collections import deque


def solution(priorities, location):
    queue = deque()
    answer = 0
    for i in range(len(priorities)):
        queue.append([priorities[i], i])

    while queue:
        now_value, now_index = queue.popleft()

        if now_value != max(priorities):
            queue.append([now_value, now_index])
        else:
            answer += 1
            if now_index == location:
                break
            else:
                priorities.remove(max(priorities))

    return answer
