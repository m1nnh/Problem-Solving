"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 퇴사
description : 삼성 기출문제
"""

import sys

sys.setrecursionlimit(10 ** 6)


def solution(times, prices, visited, day, benefit):
    global answer

    if day == len(times):
        answer = max(answer, benefit)
        return

    for i in range(day, len(times)):
        if visited[i] is False and times[i] + i <= len(times):
            visited[i] = True
            benefit += prices[i]
            solution(times, prices, visited, i + times[i], benefit)
            visited[i] = False
            benefit -= prices[i]
        else:
            solution(times, prices, visited, day + 1, benefit)


if __name__ == "__main__":
    global answer
    answer = 0
    N = int(input())
    times, prices = [], []
    visited = [False] * N

    for i in range(N):
        T, P = map(int, input().split())
        times.append(T)
        prices.append(P)

    solution(times, prices, visited, 0, 0)
    print(answer)
