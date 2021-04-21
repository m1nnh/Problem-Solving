"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 탈출
description : BFS
"""

from collections import deque
import sys

input = sys.stdin.readline


def BFS(water_position, hedgehog_position):
    water_queue = deque()
    hedgehog_queue = deque()
    hy, hx = hedgehog_position[0][0], hedgehog_position[0][1]

    for y, x in water_position:
        water_queue.append((y, x))

    hedgehog_queue.append((0, hy, hx))
    now = 0

    while hedgehog_queue:
        now_cost, now_hedgehog_y, now_hedgehog_x = hedgehog_queue.popleft()
        length = len(water_queue)

        if now <= now_cost:
            for _ in range(length):
                now_water_y, now_water_x = water_queue.popleft()
                for i in range(4):
                    nwy = dy[i] + now_water_y
                    nwx = dx[i] + now_water_x

                    if 0 <= nwy < R and 0 <= nwx < C:
                        if graph[nwy][nwx] not in ['*', 'X', 'D']:
                            graph[nwy][nwx] = '*'
                            water_queue.append((nwy, nwx))
            now += 1

        for i in range(4):
            ncost = now_cost + 1
            nhy = dy[i] + now_hedgehog_y
            nhx = dx[i] + now_hedgehog_x

            if 0 <= nhy < R and 0 <= nhx < C:
                if graph[nhy][nhx] not in ['*', 'X', 'T', 'S']:
                    if graph[nhy][nhx] == 'D':
                        return ncost
                    else:
                        graph[nhy][nhx] = 'S'
                        graph[now_hedgehog_y][now_hedgehog_x] = 'T'
                        hedgehog_queue.append((ncost, nhy, nhx))
    return 'KAKTUS'


R, C = map(int, input().split())
graph = []

hedgehog = []
water = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(R):
    graph.append(list(map(str, input())))

for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            water.append((i, j))
        elif graph[i][j] == 'S':
            hedgehog.append((i, j))
        else:
            continue

print(BFS(water, hedgehog))
