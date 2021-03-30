"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 위상 정렬 알고리즘
"""

from collections import deque

V, E = map(int, input().split())

indegree = [0] * (V + 1)
graph = [[] for i in range(V + 1)]

for i in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1


def topology_sort():
    result = []
    queue = deque()

    for i in range(1, V + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        now = queue.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
