"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 카펫
description : 완전 탐색
"""

from collections import deque


def solution(brown, yellow):
    if brown == 8:
        return [3, 3]

    answer = []
    dx = [1, 0]
    dy = [0, 1]

    queue = deque()
    queue.append((4, 3))
    dic = {(4, 3): 12}
    while queue:

        now_x, now_y = queue.popleft()
        if now_x * now_y == brown + yellow and ((now_x * 2) + (now_y * 2)) - 4 == brown:
            answer.append(now_x)
            answer.append(now_y)
            break
        elif now_x == now_y:
            continue
        else:
            for i in range(2):
                nx = dx[i] + now_x
                ny = dy[i] + now_y
                if nx * ny <= brown + yellow and (nx * 2) + (ny * 2) - 4 <= brown:
                    if (nx, ny) not in dic:
                        dic[(nx, ny)] = nx * ny
                        queue.append((nx, ny))

    return answer
