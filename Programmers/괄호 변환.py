"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 괄호 변환
description : 시뮬레이션
"""

from collections import deque


def is_correct(string):
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        elif stack:
            stack.pop()
    return not stack


def reverse(u):
    return "".join([")" if s == "(" else "(" for s in u])


def detatch(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:
        u += queue.popleft()
        if u[-1] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = "".join(list(queue))
    return u, v


def recursive(string):
    if string == "":
        return ""

    u, v = detatch(string)
    if is_correct(u):
        return u + recursive(v)
    else:
        return "(" + recursive(v) + ")" + reverse(u[1: -1])


def solution(p):
    return p if is_correct(p) else recursive(p)
