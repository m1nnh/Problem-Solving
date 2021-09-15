"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : N-Queen
description : dfs, 재귀
"""


def dfs(queen, n, row):
    count = 0

    if n == row:
        return 1

    for col in range(n):
        queen[row] = col

        for x in range(row):
            if queen[x] == queen[row]:
                break

            if abs(queen[x] - queen[row]) == (row - x):
                break

        else:
            count += dfs(queen, n, row + 1)

    return count


def solution(n):
    answer = dfs([0] * n, n, 0)
    return answer

if __name__ == "__main__":
    solution(4)