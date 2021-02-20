"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 케빈 베이컨의 6단계 법칙
description : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 플로이드-와샬
"""

N, M = map(int, input().split())
graph = [[int(1e9)] * (N + 1) for _ in range(N + 1)]
result = [int(1e9)] * (N + 1)

for x in range(1, N + 1):
    for y in range(1, N + 1):
        if x == y:
            graph[x][y] = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N + 1):
    sum_value = 0
    for j in graph[i]:
        sum_value += j
    sum_value -= int(1e9)
    result[i] = sum_value

print(result.index(min(result)))
