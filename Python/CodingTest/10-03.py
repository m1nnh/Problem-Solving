"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 개선된 서로소 집합 알고리즘
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


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    A, B = map(int, input().split())
    union_parent(parent, A, B)

print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, N + 1):
    print(find_parent(parent, i), end=' ')
print()

print('부모 테이블: ', end=' ')
for i in range(1, N + 1):
    print(parent[i], end=' ')
