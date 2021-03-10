"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 카잉 달력
description : 수학, 정수론, 중국인의 나머지 정리
"""
import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())
    if x == M:
        x = 0
    if y == N:
        y = 0

    result = -1
    for i in range(x, N * M + 1, M):
        if i % N == y:
            result = i
            break
    print(result)
