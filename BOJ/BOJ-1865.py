"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 웜홀
description : 벨만 포드
"""


def Bellman_Ford(N, distance, graph):
    distance[1] = 0

    for check in range(N):
        for vertex in range(1, N + 1):
            for next_cost, next_vertex in graph[vertex]:
                if distance[next_vertex] > distance[vertex] + next_cost:
                    distance[next_vertex] = distance[vertex] + next_cost
                    if check == N - 1:
                        return False
    return True


TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    distance = [int(1e9)] * (N + 1)

    for _ in range(M):
        node_a, node_b, cost = map(int, input().split())
        graph[node_a].append((cost, node_b))
        graph[node_b].append((cost, node_a))

    for _ in range(W):
        node_start, node_end, cost = map(int, input().split())
        graph[node_start].append((-cost, node_end))

    if Bellman_Ford(N, distance, graph):
        print('NO')
    else:
        print('YES')
