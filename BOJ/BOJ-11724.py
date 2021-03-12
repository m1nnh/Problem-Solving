"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 연결 요소의 개수
description : BFS
"""

from collections import deque


def BFS(start, visited):
    if visited[start] is True:
        return False

    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] is False:
                queue.append(i)
                visited[i] = True
    return True


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = 0

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N + 1):
    if BFS(i, visited) is True:
        result += 1
print(result)
