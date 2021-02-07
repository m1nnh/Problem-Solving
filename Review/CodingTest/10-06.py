"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 위상정렬
"""

from collections import deque


def topology_sort():
    result = []
    queue = deque()

    for i in range(1, v + 1):
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


v, e = map(int, input().split())

indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort()
