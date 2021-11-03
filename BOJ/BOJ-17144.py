"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 미세먼지 안녕!
description : 시뮬레이션
"""

from collections import defaultdict
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread(x, y, R, C):
    global room, temp_room
    count = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if room[nx][ny] > -1:
                temp_room[nx][ny] += room[x][y] // 5
                count += 1

    return count


def right(x, C):
    global room
    last = room[x][-1]

    if C > 2:
        room[x] = [-1, 0] + room[x][1: C - 1]
    else:
        room[x] = [-1, 0]

    return last


def up(x, R, right_last1, flag):
    global room
    last = room[R][flag]

    if C > 2:
        temp = [right_last1]
        for i in range(x - 1, R - 1, -1):
            temp.append(room[i][flag])
        idx = 0
        for i in range(x - 1, R - 1, -1):
            room[i][flag] = temp[idx]
            idx += 1
    else:
        room[R][flag] = right_last1

    return last


def left(x, C, last):
    global room
    left_last = room[x][0]

    if C > 2:
        room[x] = room[x][1: C - 1] + [last] + [room[x][-1]]
    else:
        room[x][0] = last

    return left_last


def down(x, R, C, flag, last):
    global room
    down_last = room[-1][-1]

    if C > 2:
        temp = [last]
        if flag == 0:
            for i in range(1, x):
                temp.append(room[i][0])
            idx = 0
            for i in range(1, x):
                room[i][0] = temp[idx]
                idx += 1
        else:
            for i in range(x + 1, R):
                temp.append(room[i][-1])
            idx = 0
            for i in range(x + 1, R):
                room[i][-1] = temp[idx]
                idx += 1

    return down_last


def rotate(cleaner, R, C):
    up_cleaner = cleaner[0]
    down_cleaner = cleaner[1]

    right_last1 = right(up_cleaner[0], C)
    up_last1 = up(up_cleaner[0], 0, right_last1, -1)
    left_last1 = left(0, C, up_last1)
    down_last1 = down(up_cleaner[0], R, C, 0, left_last1)

    right_last2 = right(down_cleaner[0], C)
    down_last2 = down(down_cleaner[0], R, C, -1, right_last2)
    left_last2 = left(R - 1, C, down_last2)
    up_last2 = up(R - 1, down_cleaner[0], left_last2, 0)
    room[down_cleaner[0]][down_cleaner[1]] = -1


def solution(R, C, T, cleaner):
    global room, temp_room
    answer = 2
    for _ in range(T):
        temp_room = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if room[i][j] >= 5:
                    count = spread(i, j, R, C)
                    room[i][j] -= ((room[i][j] // 5) * count)

        for i in range(R):
            for j in range(C):
                room[i][j] += temp_room[i][j]
        rotate(cleaner, R, C)

    for i in range(R):
        answer += sum(room[i])

    return answer


if __name__ == "__main__":
    global room
    R, C, T = map(int, input().split())
    room = []
    cleaner = []
    for i in range(R):
        A = list(map(int, input().split()))

        if -1 in A:
            cleaner.append([i, A.index(-1)])
        room.append(A)

    print(solution(R, C, T, cleaner))
