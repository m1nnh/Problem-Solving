"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 경쟁적 전염
description : DFS/BFS
"""

from collections import deque


def BFS(graph, virus_zone):
    queue = deque()

    queue.append(virus_zone)
    count = 0

    while queue:
        A = []
        if count == S:
            break
        now = queue.popleft()
        now.sort()
        for z, x, y in now:
            for j in range(4):
                nx = dx[j] + x
                ny = dy[j] + y
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        A.append((z, nx, ny))
        queue.append(A)
        count += 1


N, K = map(int, input().split())
graph = []
virus_zone = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus_zone.append((graph[i][j], i, j))

S, X, Y = map(int, input().split())
BFS(graph, virus_zone)
print(graph[X - 1][Y - 1])
