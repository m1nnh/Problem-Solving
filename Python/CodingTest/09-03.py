"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 플로이드 워셜 알고리즘
"""

N = int(input())
M = int(input())

graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A][B] = C

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == int(1e9):
            print("INFINITY", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
