"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 섬 연결하기
description : 크루스칼 알고리즘
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    answer = 0
    parent = [0] * n
    edges = []

    for i in range(n):
        parent[i] = i

    for cost in costs:
        edges.append((cost[2], cost[0], cost[1]))

    edges.sort()

    for edge in edges:
        cost, start_node, end_node = edge

        if find_parent(parent, start_node) != find_parent(parent, end_node):
            union_parent(parent, start_node, end_node)
            answer += cost

    return answer
