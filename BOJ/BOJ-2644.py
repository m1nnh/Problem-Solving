"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 촌수계산
description : DFS/BFS
"""

from collections import deque


def BFS(A, visited):
    queue = deque()
    queue.append((A, 0))
    visited[A] = True

    while queue:
        now, cnt = queue.popleft()
        if now == B:
            return cnt
        for i in graph[now]:
            if visited[i] is False:
                queue.append((i, cnt + 1))
                visited[i] = True

    return -1


N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    C, D = map(int, input().split())
    graph[C].append(D)
    graph[D].append(C)

visited = [False] * (N + 1)

result = BFS(A, visited)
print(result)
