"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 타겟 넘버
description : BFS
"""

from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()

    queue.append([numbers[0], 0])
    queue.append([- numbers[0], 0])

    while queue:
        now, index = queue.popleft()
        index += 1
        if index < len(numbers):
            queue.append([now + numbers[index], index])
            queue.append([now - numbers[index], index])
        else:
            if now == target:
                answer += 1

    return answer
