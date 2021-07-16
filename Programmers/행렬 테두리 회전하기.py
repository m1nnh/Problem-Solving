"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 행렬 테두리 회전하기
description : 구현
"""


def solution(rows, columns, queries):
    answer = []
    board = [[] for _ in range(rows)]

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            board[i - 1].append((i - 1) * columns + j)

    for x1, y1, x2, y2 in queries:
        temp = board[x1 - 1][y2 - 1]
        min_value = 10001

        # 북쪽
        min_value = min(min(board[x1 - 1][y1 - 1: y2 - 1]), min_value)
        board[x1 - 1][y1: y2] = board[x1 - 1][y1 - 1: y2 - 1]

        # 서쪽
        for i in range(x1, x2):
            min_value = min(board[i][y1 - 1], min_value)
            board[i - 1][y1 - 1] = board[i][y1 - 1]

        # 남쪽
        min_value = min(min(board[x2 - 1][y1: y2]), min_value)
        board[x2 - 1][y1 - 1: y2 - 1] = board[x2 - 1][y1: y2]

        # 동쪽
        for i in range(x2 - 2, x1 - 2, -1):
            min_value = min(board[i][y2 - 1], min_value)
            board[i + 1][y2 - 1] = board[i][y2 - 1]

        board[x1][y2 - 1] = temp
        answer.append(min(min_value, temp))

    return answer
