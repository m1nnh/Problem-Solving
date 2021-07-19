"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 거리두기 확인하기
description : BFS
"""

from collections import deque


def bfs(y, x, place):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False for _ in range(5)] for _ in range(5)]
    queue = deque()
    queue.append([y, x])
    visited[y][x] = True

    while queue:
        now_y, now_x = queue.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] is False:
                dist = abs(nx - x) + abs(ny - y)
                if place[ny][nx] != "X" and dist <= 2:
                    if place[ny][nx] == "P":
                        return False
                    else:
                        queue.append([ny, nx])
                        visited[ny][nx] = True
    return True


def solution(places):
    answer = []
    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if bfs(i, j, place) is False:
                        flag = False
                        break
            if flag is False:
                break
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer
