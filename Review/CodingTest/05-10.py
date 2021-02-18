"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 음료수 얼려 먹기
description : DFS
"""


def DFS(x, y):
    if x <= -1 or y <= -1 or x >= N or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        DFS(x - 1, y)
        DFS(x + 1, y)
        DFS(x, y - 1)
        DFS(x, y + 1)
        return True
    return False


N, M = map(int, input().split())
graph = []
result = 0
for i in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if DFS(i, j) is True:
            result += 1

print(result)
