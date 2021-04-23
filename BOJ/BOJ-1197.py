"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최소 스패닝 트리
description : 최소 스패닝 트리
"""

import sys
input = sys.stdin.readline

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


V, E = map(int, input().split())
graph = []
parent = [0] * (V + 1)

for i in range(1, V + 1):
    parent[i] = i

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))

graph.sort()
result = 0

for edge in graph:
    cost, A, B = edge

    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += cost

print(result)
