"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 감시
description : 구현, 완전탐색
"""


def plus_up(y, nx):
    global room
    while nx >= 0:
        if room[nx][y] == 200:
            break
        elif room[nx][y] != 100:
            room[nx][y] += 1
        nx -= 1

    return nx


def minus_up(x, y, nx):
    global room
    nx += 1
    while x != nx:
        if room[nx][y] != 100:
            room[nx][y] -= 1
        nx += 1


def plus_down(y, nx, N):
    global room
    while nx < N:
        if room[nx][y] == 200:
            break
        elif room[nx][y] != 100:
            room[nx][y] += 1
        nx += 1
    return nx


def minus_down(x, y, nx):
    global room
    nx -= 1
    while x != nx:
        if room[nx][y] != 100:
            room[nx][y] -= 1
        nx -= 1


def plus_left(x, ny):
    global room
    while ny >= 0:
        if room[x][ny] == 200:
            break
        elif room[x][ny] != 100:
            room[x][ny] += 1
        ny -= 1
    return ny


def minus_left(x, y, ny):
    global room
    ny += 1
    while y != ny:
        if room[x][ny] != 100:
            room[x][ny] -= 1
        ny += 1


def plus_right(x, ny, M):
    global room
    while ny < M:
        if room[x][ny] == 200:
            break
        elif room[x][ny] != 100:
            room[x][ny] += 1
        ny += 1
    return ny


def minus_right(x, y, ny):
    global room
    ny -= 1
    while y != ny:
        if room[x][ny] != 100:
            room[x][ny] -= 1
        ny -= 1


def solution(N, M, cctv_list, start):
    global answer, room

    if start == len(cctv_list):
        count = 0
        for i in range(N):
            for j in range(M):
                if room[i][j] == 0:
                    count += 1
        answer = min(answer, count)

    for i in range(start, len(cctv_list)):
        x, y = cctv_list[i][0], cctv_list[i][1]
        start += 1
        if cctv_list[i][-1] == 1:
            nx = x - 1
            nx = plus_up(y, nx)
            solution(N, M, cctv_list, start)
            minus_up(x, y, nx)
            nx = x + 1
            nx = plus_down(y, nx, N)
            solution(N, M, cctv_list, start)
            minus_down(x, y, nx)
            ny = y - 1
            ny = plus_left(x, ny)
            solution(N, M, cctv_list, start)
            minus_left(x, y, ny)
            ny = y + 1
            ny = plus_right(x, ny, M)
            solution(N, M, cctv_list, start)
            minus_right(x, y, ny)
        elif cctv_list[i][-1] == 2:
            nx1, nx2 = x - 1, x + 1
            nx1, nx2 = plus_up(y, nx1), plus_down(y, nx2, N)
            solution(N, M, cctv_list, start)
            minus_up(x, y, nx1)
            minus_down(x, y, nx2)
            ny1, ny2 = y - 1, y + 1
            ny1, ny2 = plus_left(x, ny1), plus_right(x, ny2, M)
            solution(N, M, cctv_list, start)
            minus_left(x, y, ny1)
            minus_right(x, y, ny2)
        elif cctv_list[i][-1] == 3:
            nx, ny = x - 1, y + 1
            nx, ny = plus_up(y, nx), plus_right(x, ny, M)
            solution(N, M, cctv_list, start)
            minus_up(x, y, nx)
            nx = x + 1
            nx = plus_down(y, nx, N)
            solution(N, M, cctv_list, start)
            minus_right(x, y, ny)
            ny = y - 1
            ny = plus_left(x, ny)
            solution(N, M, cctv_list, start)
            minus_down(x, y, nx)
            nx = x - 1
            nx = plus_up(y, nx)
            solution(N, M, cctv_list, start)
            minus_up(x, y, nx)
            minus_left(x, y, ny)
        elif cctv_list[i][-1] == 4:
            nx, ny1, ny2 = x - 1, y - 1, y + 1
            nx = plus_up(y, nx)
            ny1 = plus_left(x, ny1)
            ny2 = plus_right(x, ny2, M)
            solution(N, M, cctv_list, start)
            minus_up(x, y, nx)
            nx = x + 1
            nx = plus_down(y, nx, N)
            solution(N, M, cctv_list, start)
            minus_left(x, y, ny1)
            nx1 = x - 1
            nx1 = plus_up(y, nx1)
            solution(N, M, cctv_list, start)
            minus_right(x, y, ny2)
            ny1 = y - 1
            ny1 = plus_left(x, ny1)
            solution(N, M, cctv_list, start)
            minus_down(x, y, nx)
            minus_up(x, y, nx1)
            minus_left(x, y, ny1)
        else:
            nx1, nx2, ny1, ny2 = x - 1, x + 1, y - 1, y + 1
            nx1, nx2, ny1, ny2 = plus_up(y, nx1), plus_down(y, nx2, N), plus_left(x, ny1), plus_right(x, ny2, M)
            solution(N, M, cctv_list, start)
            minus_up(x, y, nx1)
            minus_down(x, y, nx2)
            minus_left(x, y, ny1)
            minus_right(x, y, ny2)
        break


if __name__ == "__main__":
    global answer, room
    answer = int(1e9)
    N, M = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(N)]
    cctv_list = []

    for i in range(N):
        for j in range(M):
            if 0 < room[i][j] < 6:
                cctv_list.append((i, j, room[i][j]))
                room[i][j] = 100
            elif room[i][j] == 6:
                room[i][j] = 200
    solution(N, M, cctv_list, 0)
    print(answer)
