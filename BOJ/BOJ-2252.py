"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 줄 세우기
description : 위상 정렬
"""

from collections import deque
import sys

input = sys.stdin.readline

def topology_sort():
    queue = deque()

    for i in range(1, N + 1):
        if ind[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for i in graph[now]:
            ind[i] -= 1

            if ind[i] == 0:
                queue.append(i)


N, M = map(int, input().split())

ind = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    ind[B] += 1

topology_sort()
