"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최솟값 만들기
description : 힙
"""

import heapq


def solution(A, B):
    answer = 0
    queueA = []
    queueB = []

    for i in range(len(A)):
        heapq.heappush(queueA, A[i])
        heapq.heappush(queueB, -B[i])

    while queueA:
        a, b = heapq.heappop(queueA), -heapq.heappop(queueB)
        answer += a * b

    return answer
