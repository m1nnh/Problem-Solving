"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 경주로 건설
description : 큐, 완전 탐색
"""

from collections import deque


def solution(board):

    queue = deque()
    queue.append((0, 0, 0, 0))

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                board[i][j] = int(1e9)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    board[0][0] = 0

    while queue:
        now_cost, now_x, now_y, now_curve = queue.popleft()

        if now_cost > board[now_x][now_y]:
            continue

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if board[nx][ny] != 1:
                    if now_x == nx:
                        if now_curve == -1 or now_curve == 0:
                            queue.append((now_cost + 100, nx, ny, -1))
                            board[nx][ny] = min(board[nx][ny], now_cost + 100)
                        else:
                            queue.append((now_cost + 600, nx, ny, -1))
                            board[nx][ny] = min(board[nx][ny], now_cost + 600)

                    else:
                        if now_curve == -2 or now_curve == 0:
                            queue.append((now_cost + 100, nx, ny, -2))
                            board[nx][ny] = min(board[nx][ny], now_cost + 100)
                        else:
                            queue.append((now_cost + 600, nx, ny, -2))
                            board[nx][ny] = min(board[nx][ny], now_cost + 600)

    answer = board[-1][-1]
    return answer