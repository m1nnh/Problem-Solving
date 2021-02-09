"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 빙산
description : DFS/BFS
"""

from collections import deque
import copy
import sys

input = sys.stdin.readline


def BFS(x, y, copy_graph):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if copy_graph[nx][ny] == 0:
                    graph[x][y] -= 1
    if graph[x][y] < 0:
        graph[x][y] = 0


def BFS_check(x, y, visited):
    if graph[x][y] == 0:
        return False
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 0 and visited[nx][ny] is False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return True


N, M = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

for i in range(N):
    graph.append(list(map(int, input().split())))

while True:
    copy_graph = copy.deepcopy(graph)
    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                BFS(i, j, copy_graph)
    count += 1
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] is False:
                if BFS_check(i, j, visited) is True:
                    result += 1
    if result >= 2:
        break
print(count)
