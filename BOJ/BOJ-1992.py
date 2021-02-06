"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 쿼드 트리
description :
"""

import sys
input = sys.stdin.readline


def quad_tree(n, x, y):
    global image, result

    first = image[y][x]

    flag = True
    for i in range(y, y + n):
        if not flag:
            break

        for j in range(x, x + n):
            if image[i][j] != first:
                result.append('(')
                quad_tree(n//2, x, y)
                quad_tree(n//2, x + n//2, y)
                quad_tree(n//2, x, y + n//2)
                quad_tree(n//2, x + n//2, y + n//2)
                result.append(')')
                flag = False
                break

    if flag:
        result.append(str(first))


N = int(input())
image = [list(map(int, input().rstrip())) for _ in range(N)]

result = []
quad_tree(N, 0, 0)

print(''.join(result))