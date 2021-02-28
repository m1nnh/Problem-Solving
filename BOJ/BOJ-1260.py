"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : DFS와 BFS
description : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
"""

from collections import deque


def DFS(graph, v, dfs_visited):
    dfs_visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if dfs_visited[i] is False:
            DFS(graph, i, dfs_visited)


def BFS(graph, v, bfs_visited):
    bfs_visited[v] = True
    queue = deque([v])

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if bfs_visited[i] is False:
                bfs_visited[i] = True
                queue.append(i)


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for x in range(1, N + 1):
    graph[x].sort()

DFS(graph, V, dfs_visited)
print()
BFS(graph, V, bfs_visited)


