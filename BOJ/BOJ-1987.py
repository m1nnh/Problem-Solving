"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 알파벳
description : DFS
"""

import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(x, y, count, visited, board):
    global answer
    visited[ord(board[x][y]) - 65] = True
    answer = max(answer, count)

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if visited[ord(board[nx][ny]) - 65] is False:
                solution(nx, ny, count + 1, visited, board)
                visited[ord(board[nx][ny]) - 65] = False


if __name__ == "__main__":
    global answer
    answer = 0
    input = sys.stdin.readline

    R, C = map(int, input().split())
    board = [list(map(str, input().strip())) for _ in range(R)]
    visited = [False] * 26

    solution(0, 0, 1, visited, board)
    print(answer)
