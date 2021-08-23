"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 가장 큰 정사각형 찾기
description : DP
"""


def solution(board):
    answer = 0

    for i in board:
        if sum(i):
            answer = 1
            break

    if answer == 0:
        return answer

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

        answer = max(answer, max(board[i]) ** 2)

    return answer
