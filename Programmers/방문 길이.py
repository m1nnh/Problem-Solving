"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 방문 길이
description : 수학
"""


def solution(dirs):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = 0, 0
    dic = {"U": 0, "D": 1, "L": 2, "R": 3}
    visited = []
    answer = 0

    for move in dirs:
        nx = dx[dic[move]] + x
        ny = dy[dic[move]] + y

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (x, y, nx, ny) not in visited:
                visited.append((x, y, nx, ny))
                visited.append((nx, ny, x, y))
                answer += 1
            x, y = nx, ny
        else:
            continue

    return answer
