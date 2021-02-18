"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : BFS
description : BFS
"""

from collections import deque


def BFS(graph, v, visited):
    queue = deque()
    visited[v] = True
    queue.append(v)
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if visited[i] is False:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

BFS(graph, V, visited)
