"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 게임 맵 최단거리
description : BFS
"""

from collections import deque


def solution(maps):
    answer = 0
    queue = deque()
    n = len(maps)
    m = len(maps[0])
    dx = [- 1, 1, 0, 0]
    dy = [0, 0, - 1, 1]
    queue.append([0, 0])

    while queue:
        now_y, now_x = queue.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if maps[ny][nx] == 1:
                    queue.append([ny, nx])
                    maps[ny][nx] = maps[now_y][now_x] + 1
    if maps[-1][-1] == 1:
        answer = -1
    else:
        answer = maps[-1][-1]
    return answer
