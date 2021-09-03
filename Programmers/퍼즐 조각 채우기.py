"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 퍼즐 조각 채우기
description : 구현
"""

import copy


def dfs(board, x, y, position, length, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    npos = [position]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < length and 0 <= ny < length:
            if board[nx][ny] == n:
                board[nx][ny] = 2
                npos = npos + dfs(board, nx, ny, [position[0] + dx[i], position[1] + dy[i]], length, n)

    return npos


def rotate(table):
    temp_table = [[0 for _ in range(len(table))] for _ in range(len(table))]

    for i in range(len(table)):
        for j in range(len(table)):
            temp_table[j][len(table) - 1 - i] = table[i][j]

    return temp_table


def solution(game_board, table):
    answer = 0

    cp_board = copy.deepcopy(game_board)
    position_block = []

    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if cp_board[i][j] == 0:
                cp_board[i][j] = 2
                result = dfs(cp_board, i, j, [0, 0], len(game_board), 0)
                position_block.append(result[1:])

    print("position block : ", position_block)

    for i in range(4):
        table = rotate(table)
        cp_table = copy.deepcopy(table)
        print(cp_table)

        for j in range(len(game_board)):
            for k in range(len(game_board)):
                if cp_table[j][k] == 1:
                    cp_table[j][k] = 2
                    result = dfs(cp_table, j, k, [0, 0], len(game_board), 1)[1:]
                    if result in position_block:
                        position_block.pop(position_block.index(result))
                        answer += len(result) + 1

                        table = copy.deepcopy(cp_table)
                    else:
                        cp_table = copy.deepcopy(table)

    return answer
