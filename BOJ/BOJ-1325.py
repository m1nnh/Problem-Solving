"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 효율적인 해킹
description : BFS
"""

from collections import deque
import sys

input = sys.stdin.readline


def BFS(start, now_visited):
    if not graph[start]:
        return
    queue = deque()
    queue.append(start)
    now_visited[start] = True
    dic[start] = 1

    while queue:
        now_computer = queue.popleft()
        for i in graph[now_computer]:
            if now_visited[i] is False:
                now_visited[i] = True
                dic[start] += 1
                queue.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dic = {}

for _ in range(M):
    computerA, computerB = map(int, input().split())
    graph[computerB].append(computerA)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    BFS(i, visited)

max_value = max(dic.values())

for i, j in dic.items():
    if j == max_value:
        print(i, end=' ')
