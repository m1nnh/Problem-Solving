"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 벽 부수고 이동하기
description : BFS
"""

from collections import deque


def BFS():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    flag = False

    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and visited[z][nx][ny] == 0:
                c = 0
                if graph[nx][ny] == 1 and z == 0:
                    visited[1][nx][ny] = visited[0][x][y] + 1
                    queue.append((nx, ny, 1))
                    c = 1
                elif graph[nx][ny] == 0:
                    visited[z][nx][ny] = visited[z][x][y] + 1
                    queue.append((nx, ny, z))

                if nx == N - 1 and ny == M - 1:
                    print(visited[z][nx][ny])
                    flag = True
                    break
        if flag == True:
            break
    if flag == False:
        print(-1)


N, M = map(int, input().split())
graph = []
idx = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

for i in range(N):
    graph.append(list(map(int, input())))
print(visited)
if N == 1 and M == 1:
    print(1)
else:
    BFS()
    print(visited)
