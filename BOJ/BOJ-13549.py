"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 숨박꼭질3
description : 위상 정렬
"""

import heapq
import sys

input = sys.stdin.readline

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, N))
    distance[N] = 0

    while queue:
        now_cost, now_position = heapq.heappop(queue)

        if now_position == K:
            min(distance[now_position], now_cost)

        if distance[now_position] < now_cost:
            continue

        if distance[now_position + 1] == int(1e9) and now_position + 1 < 100001:
            heapq.heappush(queue, (now_cost + 1, now_position + 1))
            distance[now_position + 1] = distance[now_position + 1] + now_cost + 1

        if distance[now_position - 1] == int(1e9) and now_position - 1 < 100001:
            heapq.heappush(queue, (now_cost + 1, now_position - 1))
            distance[now_position - 1] = distance[now_position - 1] + now_cost + 1

        if now_position < K and now_position * 2 < 100001:
            if distance[now_position * 2] == int(1e9):
                heapq.heappush(queue, (now_cost, now_position * 2))
                distance[now_position * 2] = now_cost


N, K = map(int, input().split())
distance = [int(1e9)] * 100001

dijkstra()

print(distance[K])

