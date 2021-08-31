"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 합승 택시 요금
description : 다익스트라
"""

import heapq


def cost_check(n, s, graph):
    distance = [int(1e9)] * (n + 1)
    distance[s] = 0
    queue = []

    heapq.heappush(queue, (0, s))

    while queue:
        now_cost, now_node = heapq.heappop(queue)

        if now_cost > distance[now_node]:
            continue

        for next_node, cost in graph[now_node]:
            next_cost = cost + now_cost

            if distance[next_node] > next_cost:
                distance[next_node] = next_cost
                heapq.heappush(queue, (next_cost, next_node))

    return distance


def solution(n, s, a, b, fares):
    answer = int(1e9)
    graph = [[] for _ in range(n + 1)]

    for i in range(len(fares)):
        graph[fares[i][0]].append([fares[i][1], fares[i][2]])
        graph[fares[i][1]].append([fares[i][0], fares[i][2]])

    org_distance = cost_check(n, s, graph)

    for i in range(1, n + 1):
        dist = cost_check(n, i, graph)
        answer = min(dist[a] + dist[b] + org_distance[i], answer)

    return answer
