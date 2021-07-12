"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 기능개발
description : 큐
"""

from collections import deque


def solution(progresses, speeds):
    answer = []
    queue = deque()

    for i in range(len(progresses)):
        now = progresses[i]
        day = 0
        while now < 100:
            day += 1
            now += speeds[i]
        queue.append(day)
    if len(queue) == 1:
        answer.append(1)
        return answer

    now = queue.popleft()
    count = 1

    while queue:
        next = queue.popleft()
        if next <= now:
            count += 1
        else:
            now = next
            answer.append(count)
            count = 1
    if count != 0:
        answer.append(count)

    return answer
