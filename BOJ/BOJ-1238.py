"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 파티
description : 다익스트라
"""

import heapq

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start][start] = 0

    while queue:
        now, time = heapq.heappop(queue)
        if distance[start][now] < time:
            continue

        for i in graph[now]:
            cost = time + i[1]

            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(queue, (i[0], cost))


N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    road_start, road_end, time = map(int, input().split())
    graph[road_start].append((road_end, time))

for i in range(1, N + 1):
    dijkstra(i)

result = 0

for i in range(1, N + 1):
    result = max(result, distance[i][X] + distance[X][i])
print(result)
