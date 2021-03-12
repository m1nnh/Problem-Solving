"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 섬의 개수
description : BFS
"""

from collections import deque


def BFS(h, w):
    if graph[h][w] == 0:
        return False
    queue = deque()
    queue.append((h, w))
    graph[h][w] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(8):
            nh = dh[i] + y
            nw = dw[i] + x
            if 0 <= nh < H and 0 <= nw < W:
                if graph[nh][nw] == 1:
                    queue.append((nh, nw))
                    graph[nh][nw] = 0
    return True


dw = [-1, 1, 0, 0, -1, 1, -1, 1]
dh = [0, 0, -1, 1, -1, -1, 1, 1]

while True:
    W, H = map(int, input().split())
    result = 0
    if W == 0 and H == 0:
        break
    graph = []
    for _ in range(H):
        graph.append(list(map(int, input().split())))

    for i in range(H):
        for j in range(W):
            if BFS(i, j) is True:
                result += 1
    print(result)
