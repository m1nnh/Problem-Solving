"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 체스판 다시 칠하기
description : 브루트포스 알고리즘
"""

n, m = map(int, input().split())

black = list('BWBWBWBW')
white = list('WBWBWBWB')

board = [list(input()) for x in range(n)]
black_start, white_start = [], []

for i in range(4):
    black_start.append(black)
    black_start.append(white)
    white_start.append(white)
    white_start.append(black)

black_count, white_count = int(1e9), int(1e9)

for i in range(n - 7):
    for j in range(m - 7):
        tmpb_count, tmpw_count = 0, 0
        for x in range(8):
            for y in range(8):
                if board[x + i][y + j] != black_start[x][y]:
                    tmpb_count += 1
                if board[x + i][y + j] != white_start[x][y]:
                    tmpw_count += 1
        black_count = min(black_count, tmpb_count)
        white_count = min(white_count, tmpw_count)

print(min(black_count, white_count))
