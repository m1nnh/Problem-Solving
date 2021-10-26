"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 트리의 순회
description : 분할정복
"""

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def solution(in_start, in_end, post_start, post_end):
    global answer, in_order, post_order, tree
    if (in_start > in_end) or (post_start > post_end):
        return

    answer.append(post_order[post_end])
    left = tree[post_order[post_end]] - in_start
    right = in_end - tree[post_order[post_end]]

    solution(in_start, in_start + left - 1, post_start, post_start + left - 1)
    solution(in_end - right + 1, in_end, post_end - right, post_end - 1)


if __name__ == "__main__":
    global answer, in_order, post_order, tree
    answer = []

    n = int(input())
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    tree = [0] * (n + 1)

    for i in range(n):
        tree[in_order[i]] = i
    solution(0, n - 1, 0, n - 1)
    print(*answer)
