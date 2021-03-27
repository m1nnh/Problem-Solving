"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 이분 그래프
description : BFS
"""

from collections import deque


def BFS(start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[now] * (-1)
            elif visited[i] == visited[now]:
                return False
    return True


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]

    for _ in range(E):
        Node_A, Node_B = map(int, input().split())
        graph[Node_A].append(Node_B)
        graph[Node_B].append(Node_A)

    flag = True
    for i in range(1, V + 1):
        if not visited[i] and not BFS(i, visited):
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')
