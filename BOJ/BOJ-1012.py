"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 유기농 배추
description : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
"""

import sys

sys.setrecursionlimit(int(1e9))

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


T = int(input())

for t in range(T):
    result = 0
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if dfs(i, j) is True:
                result += 1
    print(result)
