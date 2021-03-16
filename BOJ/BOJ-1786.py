"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 찾기
description : KMP
"""


def pi():
    pi = [0 for _ in range(0, len(P))]

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]

        if (P[i] == P[j]):
            j += 1
            pi[i] = j
    return pi


def get_pi(pi):
    result = []
    count = 0

    j = 0

    for i in range(0, len(T)):

        while j > 0 and T[i] != P[j]:
            j = pi[j - 1]

        if T[i] == P[j]:
            if j == (len(P) - 1):
                result.append(i - len(P) + 2)
                count += 1
                j = pi[j]
            else:
                j += 1
    print(count)

    for i in result:
        print(i)


T = input()
P = input()
get_pi(pi())
