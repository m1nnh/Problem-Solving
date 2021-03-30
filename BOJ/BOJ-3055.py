"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 탈출
description :
"""

R, C = map(int, input().split())
graph = []
water_position = []
hedgehog_position = []
Beaverhall_position = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(R):
    graph.append(list(map(str, input())))

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'X':