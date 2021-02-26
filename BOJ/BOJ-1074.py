"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Z
description : 분할 정복, 재귀
"""

import sys

def recursive_function(x, y, length):
    global count
    if x == r and y == c:
        print(count)
        return

    if length == 1:
        count += 1
        return

    if not (x <= r < x + length and y <= c < y + length):
        count += length * length
        return

    recursive_function(x, y, length // 2)
    recursive_function(x, y + length // 2, length // 2)
    recursive_function(x + length // 2, y, length // 2)
    recursive_function(x + length // 2, y + length // 2, length // 2)


N, r, c = map(int, sys.stdin.readline().split())
count = 0
recursive_function(0, 0, 2 ** N)
