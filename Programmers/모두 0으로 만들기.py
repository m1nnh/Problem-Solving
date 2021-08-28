"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 모두 0으로 만들기
description : dfs, 재귀
"""

from collections import defaultdict
import sys

sys.setrecursionlimit(300000)
answer = 0


def dfs(x, a, tree_dic, visited):
    global answer
    visited[x] = True

    for i in tree_dic[x]:
        if visited[i] is False:
            a[x] += dfs(i, a, tree_dic, visited)

    answer += abs(a[x])

    return a[x]


def solution(a, edges):
    global answer

    if sum(a) != 0:
        return -1

    tree_dic = defaultdict(list)
    visited = [False] * len(a)

    for edge in edges:
        tree_dic[edge[0]].append(edge[1])
        tree_dic[edge[1]].append(edge[0])

    dfs(0, a, tree_dic, visited)

    return answer
