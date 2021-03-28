"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최단 경로
description : 다익스트라
"""

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start_number):
    queue = []
    heapq.heappush(queue, (0, start_number))
    distance[start_number] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        for now_cost, next_node in graph[now]:
            next_cost = distance[now] + now_cost

            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(queue, (next_cost, next_node))


V, E = map(int, input().split())
start_number = int(input())

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    start_node, end_node, cost = map(int, input().split())
    graph[start_node].append((cost, end_node))

dijkstra(start_number)
[print(distance[node_number]) if distance[node_number] < INF else print('INF') for node_number in
 range(1, V + 1)]
