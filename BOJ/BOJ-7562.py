"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 나이트의 이동
description : BFS
"""

from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] is False:
                    queue.append((nx, ny, cnt + 1))
                    graph[nx][ny] = cnt + 1
                    visited[nx][ny] = True


T = int(input())
dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, -1, 1, -1, 1]

for i in range(T):
    N = int(input())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    BFS(A, B)
    print(graph[C][D])
