"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 거짓말
description : 그래프
"""

from collections import deque

N, M = map(int, input().split())
True_Person = list(map(int, input().split()))[1:]
graph = [list(map(int, input().split()))[1:] for _ in range(M)]

people = [False] * (N + 1)
party = [False] * M

for Person in True_Person:
    queue = deque()
    queue.append(Person)
    people[Person] = True

    while queue:
        value = queue.popleft()
        for i in range(len(graph)):
            if value in graph[i]:
                for j in graph[i]:
                    if not people[j]:
                        queue.append(j)
                        people[j] = True
                    party[i] = True

print(party.count(False))
