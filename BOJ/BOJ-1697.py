"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 숨바꼭질
description : 수학, 임의 정밀도/ 큰 수 연산
"""

from collections import deque


def BFS(N, K, visited):
    visited[N] = 1
    count = 0
    queue = deque()
    queue.append((N, count))

    while queue:
        now, cnt = queue.popleft()
        if now == K:
            return cnt
        for i in (now + 1, now - 1, now * 2):
            if 0 <= i <= 100000 and i not in visited:
                queue.append((i, cnt + 1))
                visited[i] = 1


N, K = map(int, input().split())
visited = dict()

print(BFS(N, K, visited))
