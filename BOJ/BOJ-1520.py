"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 내리막 길
description : DFS
"""

import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(x, y, graph):
    global answer

    if x == len(graph) - 1 and y == len(graph[0]) - 1:
        answer += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if graph[x][y] > graph[nx][ny]:
                solution(nx, ny, graph)
    return

if __name__ == "__main__":
    global answer
    answer = 0
    input = sys.stdin.readline
    M, N = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(M)]
    solution(0, 0, graph)

    print(answer)
