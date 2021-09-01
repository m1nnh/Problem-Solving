"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 숫자 게임
description : 힙
"""

import heapq


def solution(A, B):
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)

    while B:
        now_a, now_b = heapq.heappop(A), heapq.heappop(B)

        if now_a < now_b:
            answer += 1
        else:
            heapq.heappush(A, now_a)

    return answer
