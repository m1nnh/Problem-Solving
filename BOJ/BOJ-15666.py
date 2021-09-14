"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : N과 M(12)
description : 백트레킹
"""


def solution(N, M, array, answer):
    global result

    if len(answer) == M:
        result.append(tuple(answer))
        return

    for i in range(len(array)):
        if len(answer) == 0:
            answer.append(array[i])
            solution(N, M, array, answer)
            answer.pop()
        elif array[i] >= answer[-1]:
            answer.append(array[i])
            solution(N, M, array, answer)
            answer.pop()


if __name__ == "__main__":
    global result

    result = []

    N, M = map(int, input().split())
    array = list(map(int, input().split()))

    array.sort()
    solution(N, M, array, [])
    sort_result = sorted(list(set(result)))

    for element in sort_result:
        print(*element)
