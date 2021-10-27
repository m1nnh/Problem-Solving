"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 치즈
description : BFS, 시뮬레이션
"""

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(N, M):
    global board
    for i in range(N):
        if board[i].count(1) > 0:
            return False
    return True


def out_check(N, M):
    global board
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue.append((0, 0))
    visited[0][0] = True
    board[0][0] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] != 1 and visited[nx][ny] is False:
                    queue.append((nx, ny))
                    board[nx][ny] = -1
                    visited[nx][ny] = True


def solution(N, M):
    global board
    answer = 0
    out_check(N, M)

    while check(N, M) is False:
        out_check(N, M)
        out_cheese = []

        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    count = 0
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if board[nx][ny] == -1:
                                count += 1
                    if count >= 2:
                        out_cheese.append([i, j])
        for x, y in out_cheese:
            board[x][y] = 0
        answer += 1

    return answer


if __name__ == "__main__":
    global board
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, M))
