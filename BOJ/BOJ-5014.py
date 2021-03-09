"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 스타트링크
description : DFS/BFS
"""

from collections import deque


def BFS():
    queue = deque()
    queue.append((S, 0))
    visited[S] = True
    while queue:
        now, cnt = queue.popleft()
        if now == G:
            return cnt
        if now < G:
            nx = U + now
            if 1 <= nx <= 1000000 and visited[nx] is False:
                queue.append((nx, cnt + 1))
                visited[nx] = True
        elif now > G:
            nx = now - D
            if 1 <= nx <= 1000000 and visited[nx] is False:
                queue.append((nx, cnt + 1))
                visited[nx] = True
    return -1


F, S, G, U, D = map(int, input().split())

visited = [False] * (1000001)
result = BFS()

if result == -1:
    print('use the stairs')
else:
    print(result)
