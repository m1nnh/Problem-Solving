"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : ACM 호텔
description : 수학, 구현, 사칙연산
"""

T = int(input())
for i in range(T):
    count = 0
    H, W, N = map(int, input().split())
    ACM = [[0 for _ in range(W)] for _ in range(H)]
    for x in range(W):
        for y in range(H):
            if ACM[y][x] == 0:
                ACM[y][x] = 1
                count += 1
            if count == N:
                if (x + 1) < 10:
                    print('{}0{}'.format(y + 1, x + 1))
                else:
                    print('{}{}'.format(y + 1, x + 1))
