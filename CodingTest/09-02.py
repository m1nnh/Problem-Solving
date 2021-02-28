"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 개선된 다익스트라 알고리즘
"""
import heapq

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N + 1)]
distance = [int(1e9)] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == int(1e9):
        print("INFINITY")
    else:
        print(distance[i])
