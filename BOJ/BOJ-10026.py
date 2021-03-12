"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 적록색약
description : BFS
"""

from collections import deque
import copy


def BFS(graph, x, y, RGB):
    if graph[x][y] != RGB:
        return False
    queue = deque()
    queue.append((x, y))
    graph[x][y] = '0'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == RGB:
                    queue.append((nx, ny))
                    graph[nx][ny] = '0'
    return True


N = int(input())

first_result = 0
second_result = 0
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(str, input())))

copy_graph = copy.deepcopy(graph)
for i in range(N):
    for j in range(N):
        if copy_graph[i][j] == 'G':
            copy_graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            if BFS(graph, i, j, 'R') is True:
                first_result += 1
        elif graph[i][j] == 'G':
            if BFS(graph, i, j, 'G') is True:
                first_result += 1
        elif graph[i][j] == 'B':
            if BFS(graph, i, j, 'B') is True:
                first_result += 1
                second_result += 1
        if copy_graph[i][j] == 'R':
            if BFS(copy_graph, i, j, 'R') is True:
                second_result += 1

print(first_result, second_result)
