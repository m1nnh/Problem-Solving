"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 내리막 길
description : DFS
"""

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(x, y):
    global M, N, graph, dp

    if x == M - 1 and y == N - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += solution(nx, ny)

    return dp[x][y]


if __name__ == "__main__":
    global dp, graph, M, N

    M, N = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(M)]
    dp = [[-1] * N for _ in range(M)]

    print(solution(0, 0))
