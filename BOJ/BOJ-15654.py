"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : N과 M(5)
description : 백트레킹
"""

def recursive_comb(N, M, array, answer):
    if len(answer) == M:
        print(*answer)
        return

    for i in range(len(array)):
        if len(answer) == 0:
            answer.append(array[i])
            recursive_comb(N, M, array, answer)
            answer.pop()

        elif array[i] not in answer:
            answer.append(array[i])
            recursive_comb(N, M, array, answer)
            answer.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    array = list(map(int, input().split()))

    array.sort()

    recursive_comb(N, M, array, [])