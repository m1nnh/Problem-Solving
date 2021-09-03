"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 블록 이동하기
description : BFS
"""

from collections import deque


def move(pos1, pos2, new_board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    next_position = []

    for i in range(4):
        npos1 = (pos1[0] + dx[i], pos1[1] + dy[i])
        npos2 = (pos2[0] + dx[i], pos2[1] + dy[i])

        if new_board[npos1[0]][npos1[1]] == 0 and new_board[npos2[0]][npos2[1]] == 0:
            next_position.append((npos1, npos2))

    if pos1[0] == pos2[0]:
        for i in [-1, 1]:
            if new_board[pos1[0] + i][pos1[1]] == 0 and new_board[pos2[0] + i][pos2[1]] == 0:
                next_position.append((pos1, (pos1[0] + i, pos1[1])))
                next_position.append((pos2, (pos2[0] + i, pos2[1])))
    else:
        for i in [-1, 1]:
            if new_board[pos1[0]][pos1[1] + i] == 0 and new_board[pos2[0]][pos2[1] + i] == 0:
                next_position.append(((pos1[0], pos1[1] + i), pos1))
                next_position.append(((pos2[0], pos2[1] + i), pos2))

    return next_position


def solution(board):
    answer = 0
    new_board = [[1 for _ in range(len(board) + 2)] for _ in range(len(board) + 2)]

    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i + 1][j + 1] = board[i][j]

    queue = deque()
    queue.append([(1, 1), (1, 2), 0])
    visited = set([(1, 1), (1, 2)])

    while queue:
        pos1, pos2, count = queue.popleft()

        if pos1 == (len(board), len(board)) or pos2 == (len(board), len(board)):
            answer = count
            break

        for position in move(pos1, pos2, new_board):
            if position not in visited:
                queue.append((*position, count + 1))
                visited.add(position)

    return answer
