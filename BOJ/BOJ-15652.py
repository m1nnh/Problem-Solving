"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : N과 M(4)
description : 순열과 조합
"""


def recursive_comb(N, M, array):
    if len(array) == M:
        print(*array)
        return

    for i in range(1, N + 1):
        if len(array) == 0:
            array.append(i)
            recursive_comb(N, M, array)
            array.pop()

        elif i >= array[-1]:
            array.append(i)
            recursive_comb(N, M, array)
            array.pop()


if __name__ == "__main__":
    N, M = map(int, input().split())
    recursive_comb(N, M, [])
