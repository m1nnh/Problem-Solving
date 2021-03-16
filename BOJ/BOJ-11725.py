"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 트리의 부모 찾기
description : BFS
"""

from collections import deque
import sys

input = sys.stdin.readline


def BFS(start, graph, visited, parent):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                parent[i] = now
                visited[i] = True
                queue.append(i)


N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
visited = [False] * (N + 1)

for i in range(N - 1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

start = 1
BFS(start, graph, visited, parent)

[print(parent[x]) for x in range(2, N + 1)]
