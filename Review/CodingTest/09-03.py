"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 플로이드 워셜
description : 플로이드 워셜
"""

N = int(input())
M = int(input())
graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    A, B, C = map(int, input().split())
    graph[A][B] = C

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            graph[j][k] = min(graph[j][k], graph[i][k] + graph[j][i])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == int(1e9):
            print('infinity', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
