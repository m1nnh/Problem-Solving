"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 숨박꼭질3
description : 다익스트라
"""

import heapq


def solution(N, K):
    global distance

    queue = []
    heapq.heappush(queue, (0, N))
    distance[N] = 0

    while queue:
        now_cost, now_position = heapq.heappop(queue)

        if now_position == K:
            return now_cost

        if now_position * 2 <= 100000 and now_cost < distance[now_position * 2]:
            distance[now_position * 2] = now_cost
            heapq.heappush(queue, (now_cost, now_position * 2))
        if now_position + 1 <= 100000 and now_cost + 1 < distance[now_position + 1]:
            distance[now_position + 1] = now_cost + 1
            heapq.heappush(queue, (now_cost + 1, now_position + 1))
        if now_position - 1 >= 0 and now_cost + 1 < distance[now_position - 1]:
            distance[now_position - 1] = now_cost + 1
            heapq.heappush(queue, (now_cost + 1, now_position - 1))


if __name__ == "__main__":
    global distance

    N, K = map(int, input().split())
    distance = [int(1e9)] * 100001

    print(solution(N, K))
