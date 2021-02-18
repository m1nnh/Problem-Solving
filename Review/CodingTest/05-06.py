"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : DFS
description : DFS
"""


def DFS(graph, v, visited):
    stack = []
    visited[v] = True
    stack.append(v)
    while stack:
        now = stack.pop()
        print(now, end=' ')
        for i in graph[now]:
            if visited[i] is False:
                stack.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

DFS(graph, V, visited)
