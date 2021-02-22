"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 스택
description : 자료구조, 스택
"""

import sys

N = int(sys.stdin.readline())

stack = []


def push(n):
    stack.append(int(n))


def size():
    print(len(stack))


def pop():
    if stack:
        pop_value = stack.pop()
        print(pop_value)
    else:
        print(-1)


def empty():
    if stack:
        print(0)
    else:
        print(1)


def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)


for i in range(N):
    String = list(map(str, sys.stdin.readline().split()))
    if String[0] == 'push':
        push(String[1])
    elif String[0] == 'pop':
        pop()
    elif String[0] == 'size':
        size()
    elif String[0] == 'empty':
        empty()
    else:
        top()
