"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 서로소 집합을 활용한 사이클 판별
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


V, E = map(int, input().split())
parent = [0] * (V + 1)
cycle = False

for i in range(1, V + 1):
    parent[i] = i

for i in range(E):
    A, B = map(int, input().split())
    if find_parent(parent, A) == find_parent(parent, B):
        cycle = True
        break
    else:
        union_parent(parent, A, B)

if cycle:
    print('cycle이 일어났습니다.')
else:
    print('cucle이 일어나지 않았습니다.')
