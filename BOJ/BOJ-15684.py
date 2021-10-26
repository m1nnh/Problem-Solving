"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 사다리 조작
description : 구현, 완전탐색
"""

import sys

input = sys.stdin.readline


def check():
    global lines, N, H
    for i in range(N):
        now = i
        for j in range(H):
            if lines[j][now] is True:
                now += 1
            elif now > 0 and lines[j][now - 1] is True:
                now -= 1
        if now != i:
            return False
    return True


def solution(x, y, count):
    global lines, answer, N, H

    if count > answer:
        return

    if check() is True:
        answer = min(answer, count)
        return

    if count == 3:
        return

    for i in range(x, H):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, N - 1):
            if lines[i][j] is False and lines[i][j + 1] is False:
                if j > 0 and lines[i][j - 1] is True:
                    continue
                lines[i][j] = True
                solution(x, j + 2, count + 1)
                lines[i][j] = False


if __name__ == "__main__":
    global answer, lines
    answer = 4

    N, M, H = map(int, input().split())

    if M == 0:
        print(0)
    else:
        lines = [[False] * N for _ in range(H)]

        for _ in range(M):
            x, y = map(int, input().split())
            lines[x - 1][y - 1] = True

        solution(0, 0, 0)

        if answer == 4:
            print(-1)
        else:
            print(answer)
