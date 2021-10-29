"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : N-Queen
description : DFS, 완전탐색
"""

import sys

input = sys.stdin.readline


def solution(board, N, row):
    answer = 0

    if row == N:
        return 1

    for i in range(N):
        board[row] = i
        for j in range(row):
            if board[j] == board[row]:
                break
            if abs(board[j] - board[row]) == (row - j):
                break
        else:
            answer += solution(board, N, row + 1)

    return answer


if __name__ == "__main__":
    N = int(input())
    board = [0] * N
    print(solution(board, N, 0))
