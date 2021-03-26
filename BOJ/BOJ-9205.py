"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 맥주 마시면서 걸어가기
description : 플로이드 와샬
"""

t = int(input())

for _ in range(t):
    mart_count = int(input())
    coord = []
    coord.append(list(map(int, input().split())))

    for _ in range(mart_count):
        coord.append(list(map(int, input().split())))
    coord.append(list(map(int, input().split())))

    graph = [[int(1e9)] * (len(coord)) for _ in range(len(coord))]

    for i in range(len(coord)):
        for j in range(len(coord)):
            if i == j:
                continue
            elif (abs(coord[i][0] - coord[j][0]) + abs(coord[i][1] - coord[j][1])) <= 1000:
                graph[i][j] = 1

    for i in range(len(coord)):
        for j in range(len(coord)):
            for k in range(len(coord)):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    if graph[0][-1] == int(1e9):
        print('sad')
    else:
        print('happy')
