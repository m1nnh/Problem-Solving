"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 영역 구하기
description : BFS/DFS
"""

from collections import deque


def BFS(y, x):
    queue = deque()
    queue.append((y, x))
    cnt = 0
    graph[y][x] = 1
    while queue:
        y, x = queue.popleft()
        cnt += 1
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < M and 0 <= nx < N:
                if graph[ny][nx] == 0:
                    queue.append((ny, nx))
                    graph[ny][nx] = 1
    return cnt


M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = []
count = 0
for _ in range(K):
    x, y, i, j = map(int, input().split())
    for z in range(y, j):
        for k in range(x, i):
            graph[z][k] = 1

for z in range(M):
    for k in range(N):
        if graph[z][k] == 0:
            result.append(BFS(z, k))
            count += 1
result.sort()
print(count)
[print(x, end=' ') for x in result]
