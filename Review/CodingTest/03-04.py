"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 1이 될 때까지
description : 그리디 알고리즘, BFS
"""

from collections import deque


def BFS(N, visited, graph):
    queue = deque()
    count = 0
    visited[N] = True
    queue.append((N, count))
    while queue:
        now, cnt = queue.popleft()
        for i in (now - 1, now // K):
            if visited[i] is False:
                queue.append((i, cnt + 1))
                visited[i] = True
                graph[i] = cnt + 1


N, K = map(int, input().split())
visited = [False] * 100000
graph = [0] * 100000
BFS(N, visited, graph)

print(graph[1])
