"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 팀결성
"""


def find_team(parent, x):
    if parent[x] != x:
        parent[x] = find_team(parent, parent[x])
    return parent[x]


def union_team(parent, a, b):
    a = find_team(parent, a)
    b = find_team(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    A, B, C = map(int, input().split())
    if A == 0:
        union_team(parent, B, C)
    else:
        if find_team(parent, B) != find_team(parent, C):
            print('NO')
        else:
            print('YES')
