"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 주사위 굴리기
description : 구현
"""


def solution(N, M, x, y, board, cmd):
    dice = [[0], [0, 0, 0], [0], [0]]
    dic = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}

    for command in cmd:
        nx = dic[command][0] + x
        ny = dic[command][1] + y
        if 0 <= nx < N and 0 <= ny < M:
            if command == 1:
                dice[1][2], dice[1][1], dice[1][0], dice[3][0] = dice[1][1], dice[1][0], dice[3][0], dice[1][2]
            elif command == 2:
                dice[1][0], dice[1][1], dice[1][2], dice[3][0] = dice[1][1], dice[1][2], dice[3][0], dice[1][0]
            elif command == 3:
                dice[0][0], dice[1][1], dice[2][0], dice[3][0] = dice[1][1], dice[2][0], dice[3][0], dice[0][0]
            else:
                dice[0][0], dice[1][1], dice[2][0], dice[3][0] = dice[3][0], dice[0][0], dice[1][1], dice[2][0]

            print(dice[1][1])

            if board[nx][ny] == 0:
                board[nx][ny] = dice[3][0]
            else:
                dice[3][0] = board[nx][ny]
                board[nx][ny] = 0
            x, y = nx, ny


if __name__ == "__main__":
    N, M, x, y, K = map(int, input().split())
    board = []

    for _ in range(N):
        board.append(list(map(int, input().split())))

    cmd = list(map(int, input().split()))

    solution(N, M, x, y, board, cmd)
