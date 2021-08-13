"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 여행경로
description : 딕셔너리, BFS
"""

from collections import defaultdict, deque
import copy


def solution(tickets):
    answer = list()
    graph = defaultdict(list)
    visited = defaultdict(int)
    dic_visited = defaultdict(int)
    for i in range(len(tickets)):
        graph[tickets[i][0]].append(tickets[i][1])
        visited[tickets[i][0] + tickets[i][1]] += 1

    for key, values in graph.items():
        graph[key] = sorted(values)

    queue = deque()
    queue.append(["ICN", ["ICN"], visited])

    while queue:
        now_ticket, now_array, now_visited = queue.popleft()
        flag = list(now_visited.values())
        if sum(flag) == 0:
            answer = now_array
            break
        for next_ticket in graph[now_ticket]:
            if now_visited[now_ticket + next_ticket] != 0:
                next_array = copy.deepcopy(now_array)
                next_array.append(next_ticket)
                if "".join(next_array) not in dic_visited:
                    next_visited = copy.deepcopy(now_visited)
                    next_visited[now_ticket + next_ticket] -= 1
                    queue.append([next_ticket, next_array, next_visited])
                    dic_visited["".join(next_array)] += 1

    return answer
