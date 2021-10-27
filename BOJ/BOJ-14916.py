"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 거스름돈
description : Greedy
"""


def solution(n):
    if n in [1, 3]:
        return -1
    if (n % 5) % 2 == 0:
        return n // 5 + (n % 5) // 2
    else:
        return ((n // 5) - 1) + ((n % 5 + 5) // 2)


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
