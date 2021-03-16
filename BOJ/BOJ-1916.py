"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최소비용 구하기
description :
"""

import heapq


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        now_cost, now_node = heapq.heappop(queue)

        if distance[now_node] < now_cost:
            continue

        for next_cost, next_node in graph[now_node]:
            new_cost = next_cost + distance[now_node]

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))


N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
distance = [int(1e9)] * (N + 1)

for _ in range(M):
    bus_start, bus_end, cost = map(int, input().split())
    graph[bus_start].append((cost, bus_end))

start, end = map(int, input().split())
dijkstra(start)

print(distance[end])
