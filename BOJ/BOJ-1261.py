"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 알고스팟
description : dijkstra
"""

import heapq

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    distance[0][0] = 0
    while queue:
        now_cost, now_x, now_y = heapq.heappop(queue)

        if now_y == N - 1 and now_x == M - 1:
            return now_cost

        if distance[now_y][now_x] < now_cost:
            continue

        for i in range(4):
            next_cost = now_cost + 1
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0 and visited[ny][nx] is False:
                    visited[ny][nx] = True
                    distance[ny][nx] = now_cost
                    heapq.heappush(queue, (now_cost, nx, ny))
                elif graph[ny][nx] == 1 and visited[ny][nx] is False:
                    visited[ny][nx] = True
                    distance[ny][nx] = next_cost
                    heapq.heappush(queue, (next_cost, nx, ny))


M, N = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
distance = [[int(1e9) for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input())))

print(dijkstra())
