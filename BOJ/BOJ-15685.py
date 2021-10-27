"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 드래곤 커브
description : 구현, 시뮬레이션
"""


def solution(x, y, d, g):
    global dragon_map, dic
    info = [d]

    for _ in range(g):
        info += [(i + 1) % 4 for i in info[::-1]]
    print(info)
    dragon_map[y][x] = 0

    nx = x
    ny = y

    for curve in info:
        nx = nx + dic[curve][1]
        ny = ny + dic[curve][0]
        dragon_map[ny][nx] = 0


if __name__ == "__main__":
    global dragon_map, dic
    N = int(input())
    dragon_map = [[1] * 101 for _ in range(101)]
    dic = {0: [0, 1], 1: [-1, 0], 2: [0, -1], 3: [1, 0]}

    for _ in range(N):
        x, y, d, g = map(int, input().split())
        solution(x, y, d, g)

    answer = 0

    for i in range(100):
        for j in range(100):
            if dragon_map[i][j] + dragon_map[i][j + 1] + dragon_map[i + 1][j] + dragon_map[i + 1][j + 1] == 0:
                answer += 1

    print(answer)
