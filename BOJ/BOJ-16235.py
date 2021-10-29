"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 나무 재테크
description : 시뮬레이션
"""

from collections import defaultdict
import sys

input = sys.stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def spring():
    global graph, dic
    die_trees = defaultdict(list)

    for key, values in dic.items():
        if len(values) == 0:
            continue

        values.sort()

        for i in range(len(values)):
            if graph[key[0]][key[1]] - values[i] >= 0:
                graph[key[0]][key[1]] -= values[i]
                values[i] += 1
            else:
                dic[(key[0], key[1])] = values[:i]
                die_trees[(key[0], key[1])] = values[i:]
                break

    return die_trees


def summer(die_trees):
    global graph

    for key, values in die_trees.items():
        for i in range(len(values)):
            graph[key[0]][key[1]] += (values[i] // 2)


def fall(N):
    global graph, dic

    for key, values in list(dic.items()):
        if len(values) == 0:
            continue

        for i in range(len(values)):
            if values[i] % 5 == 0:
                for j in range(8):
                    nx = key[0] + dx[j]
                    ny = key[1] + dy[j]
                    if 0 <= nx < N and 0 <= ny < N:
                        dic[(nx, ny)].append(1)


def winter():
    global A, graph

    for i in range(len(A)):
        for j in range(len(A[0])):
            graph[i][j] += A[i][j]


def solution(N, M, K):
    global dic
    answer = 0

    for i in range(K):
        die_trees = spring()
        summer(die_trees)
        fall(N)
        winter()

    for key, values in dic.items():
        if len(values) == 0:
            continue
        else:
            answer += len(values)

    return answer


if __name__ == "__main__":
    global graph, dic, A

    N, M, K = map(int, input().split())
    graph = [[5] * N for _ in range(N)]
    A = [list(map(int, input().split())) for _ in range(N)]
    dic = defaultdict(list)

    for _ in range(M):
        x, y, z = map(int, input().split())
        dic[(x - 1, y - 1)].append(z)

    print(solution(N, M, K))
