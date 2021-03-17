"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 정수 삼각형
description : 다이나믹 프로그래밍
"""

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

k = 2

for i in range(1, N):
    for j in range(k):
        if j == 0:
            graph[i][j] = graph[i][j] + graph[i - 1][j]
        elif i == j:
            graph[i][j] = graph[i][j] + graph[i - 1][j - 1]
        else:
            graph[i][j] = max(graph[i - 1][j - 1], graph[i - 1][j]) + graph[i][j]
    k += 1

print(max(graph[N - 1]))
