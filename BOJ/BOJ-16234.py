"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 인구 이동
description : BFS, 완전탐색
"""

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(N, L, R, x, y):
    global visited, board
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    union_country = [x, y]

    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] is False and L <= abs(board[nx][ny] - board[now_x][now_y]) <= R:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    union_country.append(nx)
                    union_country.append(ny)
    return union_country


def solution(N, L, R):
    global visited
    answer = 0

    while True:
        visited = [[False for _ in range(N)] for _ in range(N)]
        check_country = []
        for i in range(N):
            for j in range(N):
                if visited[i][j] is False:
                    union_country = check(N, L, R, i, j)
                    if len(union_country) > 2:
                        check_country.append(union_country)

        if len(check_country) > 0:
            answer += 1
            for i in range(len(check_country)):
                sum_value = 0
                count_country = len(check_country[i]) // 2
                for j in range(0, len(check_country[i]), 2):
                    sum_value += board[check_country[i][j]][check_country[i][j + 1]]
                for k in range(0, len(check_country[i]), 2):
                    board[check_country[i][k]][check_country[i][k + 1]] = sum_value // count_country
        else:
            break

    return answer


if __name__ == "__main__":
    global board
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, L, R))
