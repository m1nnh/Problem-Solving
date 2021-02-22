"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 덱
description :
"""
"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 큐
description : 자료구조, 큐
"""

from collections import deque
import sys

queue = deque()


def push(string, X):
    if string == 'push_front':
        queue.appendleft(int(X))
    else:
        queue.append(int(X))


def pop(string):
    pop_value = 0
    if queue:
        if string == 'pop_front':
            pop_value = queue.popleft()
            print(pop_value)
        else:
            pop_value = queue.pop()
            print(pop_value)
    else:
        print(-1)


def size():
    if queue:
        print(len(queue))
    else:
        print(0)


def empty():
    if queue:
        print(0)
    else:
        print(1)


def front():
    if queue:
        print(queue[0])
    else:
        print(-1)


def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)


N = int(sys.stdin.readline())

for i in range(N):
    String = list(map(str, sys.stdin.readline().split()))
    if 'push' in String[0]:
        push(String[0], String[1])
    elif 'pop' in String[0]:
        pop(String[0])
    elif String[0] == 'size':
        size()
    elif String[0] == 'empty':
        empty()
    elif String[0] == 'front':
        front()
    else:
        back()
