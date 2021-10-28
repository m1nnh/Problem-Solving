"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 스티커
description : 다이나믹프로그래밍
"""


def solution(board, n):
    for i in range(1, n):
        if i == 1:
            board[0][i] += board[1][i - 1]
            board[1][i] += board[0][i - 1]
        else:
            board[0][i] += max(board[1][i - 1], board[1][i - 2])
            board[1][i] += max(board[0][i - 1], board[0][i - 2])

    return max(board[0][n - 1], board[1][n - 1])


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(2)]
        print(solution(board, n))
