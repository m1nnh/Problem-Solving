"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 이진 검색 트리
description : 재귀
"""

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def solution(trees):
    if len(trees) <= 1:
        return trees

    for i in range(1, len(trees)):
        if trees[i] > trees[0]:
            return solution(trees[1: i]) + solution(trees[i:]) + [trees[0]]

    return solution(trees[1:]) + [trees[0]]


if __name__ == "__main__":
    trees = []
    while True:
        try:
            trees.append(int(input()))
        except:
            break

    post_order = solution(trees)
    for i in range(len(post_order)):
        print(post_order[i])
