"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : DFS
"""

graph = [[], [2, 3, 8], [1, 7, 8], [1, 4, 5], [3, 5], [3, 4], [7], [6, 8], [1, 7]]

visited = [False] * 9


def dfs(Graph, v, Visited):
    Visited[v] = True
    print(v, end=' ')

    for i in Graph[v]:
        if Visited[i] is False:
            dfs(Graph, i, Visited)


dfs(graph, 1, visited)
