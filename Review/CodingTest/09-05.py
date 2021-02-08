"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 전보
description : 다익스트라
"""

import heapq


def dijkstra(C):
    queue = []
    heapq.heappush(queue, (C, 0))
    distance[C] = 0

    while queue:
        now, dist = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))


N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [int(1e9)] * (N + 1)

for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

dijkstra(C)

count = 0
max_distance = 0

for d in distance:
    if d != int(1e9):
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
