"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : N과 M(4)
description : 순열과 조합
"""


def comb(count, array):
    if count > M:
        for i in array:
            print(i, end=' ')
        print()
        return

    for i in range(1, N + 1):
        if len(array) == 0:
            array.append(i)
            comb(count + 1, array)
            array.remove(i)

        elif i >= array[-1]:
            array.append(i)
            comb(count + 1, array)
            array.remove(i)


N, M = map(int, input().split())

comb(1, [])
