"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 미로 탈출
description : BFS
"""

from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        n, m = queue.popleft()
        for i in range(4):
            nx = n + dx[i]
            ny = m + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[n][m] + 1
                queue.append((nx, ny))
    return graph[N - 1][M - 1]


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
print(BFS(0, 0))
