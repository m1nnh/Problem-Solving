"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : BFS
"""

from collections import deque

graph = [[], [2, 3, 8], [1, 7, 8], [1, 4, 5], [3, 5], [3, 4], [7], [6, 8], [1, 7]]
visited = [False] * 9


def bfs(Graph, s, Visited):
    queue = deque([s])
    Visited[s] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in Graph[v]:
            if Visited[i] is False:
                queue.append(i)
                Visited[i] = True


bfs(graph, 1, visited)
