"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : N과 M(9)
description : 백트레킹
"""


def recursive_comb(N, M, array, answer, index):
    if len(answer) == M:
        result.append(tuple(answer))
        return

    for i in range(len(array)):
        if i not in index:
            answer.append(array[i])
            index.append(i)
            recursive_comb(N, M, array, answer, index)
            answer.pop()
            index.pop()


if __name__ == "__main__":

    global result
    result = []
    
    N, M = map(int, input().split())
    array = list(map(int, input().split()))

    array.sort()

    recursive_comb(N, M, array, [], [])
    sort_result = sorted(list(set(result)))

    for element in sort_result:
        print(*element)
