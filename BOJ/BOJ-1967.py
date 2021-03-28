"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 트리의 지름
description : 다익스트라
"""

import heapq


def dijkstra(start):
    distance = [int(1e9)] * (N + 1)
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

    return distance


N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    node_parent, node_child, cost = map(int, input().split())
    graph[node_parent].append((cost, node_child))
    graph[node_child].append((cost, node_parent))

first_dijkstra = dijkstra(1)[1:]
new_start = first_dijkstra.index(max(first_dijkstra)) + 1
second_dijkstra = dijkstra(new_start)[1:]

print(max(second_dijkstra))
