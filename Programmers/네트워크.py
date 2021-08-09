"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 네트워크
description : BFS
"""
from collections import deque


def bfs(number, visited, computers):
    queue = deque()
    queue.append(number)
    visited[number] = True

    while queue:
        now = queue.popleft()

        for i in range(len(computers)):
            if i == now:
                continue
            elif computers[now][i] == 1:
                if visited[i] is False:
                    visited[i] = True
                    queue.append(i)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for number in range(n):
        if visited[number] is False:
            bfs(number, visited, computers)
            answer += 1

    return answer
