"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 알바생 강호
description : Greedy
"""

N = int(input())
result = 0
graph = []
for i in range(N):
    graph.append(int(input()))

graph.sort(reverse=True)
for i in range(N):
    if graph[i] - i > 0:
        result += graph[i] - i

print(result)
