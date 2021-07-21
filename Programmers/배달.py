"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 배달
description : 최단 경로
"""

import heapq


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    distance = [int(1e9)] * (N + 1)
    queue = []

    for x, y, cost in road:
        graph[x].append([cost, y])
        graph[y].append([cost, x])

    heapq.heappush(queue, [0, 1])
    distance[1] = 0

    while queue:
        now_cost, now_node = heapq.heappop(queue)
        if now_cost > distance[now_node]:
            continue

        for node_graph in graph[now_node]:
            next_cost = now_cost + node_graph[0]
            next_node = node_graph[1]

            if next_cost < distance[next_node]:
                heapq.heappush(queue, [next_cost, next_node])
                distance[next_node] = next_cost

    for i in range(1, len(distance)):
        if distance[i] <= K:
            answer += 1

    return answer
