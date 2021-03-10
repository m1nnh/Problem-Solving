"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 색종이 만들기
description : 재귀함수, 분할정복
"""


def recursive(n, x, y):
    global blue, white
    color = graph[x][y]
    flag = True

    for i in range(x, x + n):
        if not flag:
            break
        for j in range(y, y + n):
            if color != graph[i][j]:
                recursive(n // 2, x, y)
                recursive(n // 2, x + n // 2, y)
                recursive(n // 2, x, y + n // 2)
                recursive(n // 2, x + n // 2, y + n // 2)
                flag = False
                break
    if flag:
        if color == 1:
            blue += 1
        else:
            white += 1


N = int(input())
graph = []

blue = 0
white = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

recursive(N, 0, 0)

print(white)
print(blue)
