"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : heapq를 이용한 다익스트라
description : 다익스트라
"""

import heapq


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start] = 0

    while queue:
        now, dist = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))


N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N + 1)]
distance = [int(1e9)] * (N + 1)

for i in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == int(1e9):
        print('infinity')
    else:
        print(distance[i])
