"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 카드 정렬하기
description : 그리디, 우선순위 큐
"""

import heapq
import sys

input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    num = int(input())
    heapq.heappush(queue, num)

result = 0

while len(queue) != 1:

    sum_value = 0

    for _ in range(2):
        sum_value += heapq.heappop(queue)

    result += sum_value
    heapq.heappush(queue, sum_value)

print(result)
