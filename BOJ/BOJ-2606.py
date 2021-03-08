"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 바이러스
description : DFS/BFS
"""


def DFS(graph, visited, start):
    count = 0
    stack = []
    stack.append(start)
    visited[start] = True
    while stack:
        now = stack.pop()
        for i in graph[now]:
            if visited[i] is False:
                stack.append(i)
                visited[i] = True
        count += 1
    return count


C = int(input())
N = int(input())
start = 1
graph = [[] for _ in range(C + 1)]
visited = [False] * (C + 1)
for i in range(N):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

print(DFS(graph, visited, start) - 1)
