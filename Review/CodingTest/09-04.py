"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 미래도시
description : 플로이드 워셜
"""

N, M = map(int, input().split())
graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for i in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

X, K = map(int, input().split())

distance = graph[1][X] + graph[X][K]

if distance >= int(1e9):
    print('못 만나')
else:
    print(distance)
