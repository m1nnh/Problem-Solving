"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 요세푸스 문제 0
description : 자료구조, 큐
"""

from collections import deque

N, K = map(int, input().split())

Josephus = []

count = 0
queue = deque(x for x in range(1, N + 1))

while queue:
    if count == 0:
        count += 1
        continue
    elif count % K == 0:
        Josephus.append(queue.popleft())
        count = 0
    else:
        front = queue.popleft()
        queue.append(front)
        count += 1

print('<{}'.format(Josephus[0]), end='')

[print(', {}'.format(Josephus[x]), end='') for x in range(1, len(Josephus))]

print('>')
