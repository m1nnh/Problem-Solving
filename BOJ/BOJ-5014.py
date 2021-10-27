"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 스타트링크
description : DFS/BFS
"""

from collections import deque


def solution(F, S, G, U, D):
    answer = int(1e9)

    visited = [False] * (F + 1)
    queue = deque()
    queue.append((S, 0))
    visited[S] = True

    while queue:
        now_position, now_cost = queue.popleft()

        if now_position == G:
            answer = min(answer, now_cost)
        if now_position + U <= F and visited[now_position + U] is False:
            queue.append((now_position + U, now_cost + 1))
            visited[now_position + U] = True
        if now_position - D > 0 and visited[now_position - D] is False:
            queue.append((now_position - D, now_cost + 1))
            visited[now_position - D] = True

    if answer == int(1e9):
        return "use the stairs"
    else:
        return answer


if __name__ == "__main__":
    F, S, G, U, D = map(int, input().split())
    print(solution(F, S, G, U, D))
