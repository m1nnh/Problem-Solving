"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 가장 먼 노드
description : 최단경로
"""

import heapq


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [int(1e9)] * (n + 1)

    for i in range(len(edge)):
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])

    distance[1] = 0
    queue = []
    heapq.heappush(queue, (0, 1))

    while queue:
        now_dist, now_node = heapq.heappop(queue)
        if distance[now_node] < now_dist:
            continue
        for i in graph[now_node]:
            next_cost = 1 + now_dist
            if next_cost < distance[i]:
                heapq.heappush(queue, (next_cost, i))
                distance[i] = next_cost

    max_value = max(distance[1:])
    answer = distance.count(max_value)

    return answer
