"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 토마토
description : BFS
"""

from collections import deque


def BFS(tomato):
    queue = deque()
    queue.append(tomato)
    count = 0
    while queue:
        A = []
        now = queue.popleft()
        for x, y in now:
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < M and 0 <= ny < N:
                    if graph[nx][ny] == 0:
                        A.append((nx, ny))
                        graph[nx][ny] = 1
        if len(A) != 0:
            queue.append(A)
            count += 1
        else:
            break
    return count


N, M = map(int, input().split())
graph = []
tomato = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(M):
    graph.append(list(map(int, input().split())))

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            tomato.append((i, j))

result = BFS(tomato)

flag = True
for i in range(M):
    if 0 in graph[i]:
        flag = False

if flag:
    print(result)
else:
    print(-1)
