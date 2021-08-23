"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [1차] 프렌즈4블록
description : 구현
"""

import copy

def check(m, n, board):
    cp_board = copy.deepcopy(board)
    total = 0

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == -1:
                continue
            if board[i][j] == board[i][j - 1] == board[i - 1][j] == board[i - 1][j - 1]:
                cp_board[i][j], cp_board[i][j - 1], cp_board[i - 1][j], cp_board[i - 1][j - 1] = 0, 0, 0, 0

    for i in range(len(cp_board)):
        count = cp_board[i].count(0)
        total += count
        array = [-1] * count

        if len(array) != 0:
            for j in range(len(cp_board[i])):
                if cp_board[i][j] != 0:
                    array.append(cp_board[i][j])
            cp_board[i] = array

    return cp_board, total


def solution(m, n, board):
    board = list(map(list, zip(*board)))
    answer = 0

    while True:
        board, count = check(m, n, board)

        if count == 0:
            break

        answer += count

    return answer
