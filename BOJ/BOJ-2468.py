"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 안전 영역
description : DFS/BFS
"""

from collections import deque
import copy


def BFS(x, y, k, copy_graph):
    if copy_graph[x][y] <= k:
        return False

    queue = deque()
    queue.append((x, y))
    copy_graph[x][y] = k
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N:
                if copy_graph[nx][ny] > k:
                    queue.append((nx, ny))
                    copy_graph[nx][ny] = k
    return True


N = int(input())
graph = []
safe_zone = []
min_value = int(1e9)
max_value = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    A = list(map(int, input().split()))
    min_value = min(min_value, min(A))
    max_value = max(max_value, max(A))
    graph.append(A)

max_zone = 1

for i in range(min_value, max_value):
    copy_graph = copy.deepcopy(graph)
    result = 0
    for j in range(N):
        for k in range(N):
            if BFS(j, k, i, copy_graph) is True:
                result += 1
    max_zone = max(max_zone, result)
print(max_zone)
