"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 단지번호붙이기
description : DFS/BFS
"""


def DFS(x, y):
    stack = []
    stack.append((x, y))
    count = 1
    graph[x][y] = 2

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] += 1
                    stack.append((nx, ny))
                    count += 1

    return count


N = int(input())
graph = []
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(DFS(i, j))

result.sort()
print(len(result))
[print(x) for x in result]
