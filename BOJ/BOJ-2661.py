"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 좋은 수열
description : 백 트레킹
"""

import heapq

def check(string):
    for i in range(1, (len(string) // 2) + 1):
        start = 0
        end = start + i
        for j in range(0, len(string) - (2 * i) + 1):
            if string[start + j: start + i + j] == string[end + j: end + i + j]:
                return False
    return True


N = int(input())
queue = []
arr = ['1', '2', '3']

heapq.heappush(queue, (-1, '1'))
flag = False

while queue:
    length, now = heapq.heappop(queue)

    for i in arr:
        result = str(now) + i

        if check(result):
            if len(result) == N:
                print(int(result))
                flag = True
                break
            else:
                heapq.heappush(queue, (-len(result), int(result)))

    if flag:
        break
