"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 특정한 최단 경로
description : 다익스트라
"""

import heapq


def dijkstra(start, end):
    distance = [int(1e9)] * (N + 1)

    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start] = 0

    while queue:
        now, dist = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))

    return distance[end]


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    node_a, node_b, dist = map(int, input().split())
    graph[node_a].append((node_b, dist))
    graph[node_b].append((node_a, dist))

node_v1, node_v2 = map(int, input().split())

result1 = dijkstra(1, node_v1) + dijkstra(node_v1, node_v2) + dijkstra(node_v2, N)
result2 = dijkstra(1, node_v2) + dijkstra(node_v2, node_v1) + dijkstra(node_v1, N)

if result1 >= int(1e9) and result2 >= int(1e9):
    print(-1)
else:
    print(min(result1, result2))
