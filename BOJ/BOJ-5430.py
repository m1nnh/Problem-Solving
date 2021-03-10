"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : AC
description : 덱, 큐, 자료구조
"""

from collections import deque

T = int(input())

for i in range(T):
    func = list(map(str, input()))
    N = int(input())
    arr = input()
    arr = arr.replace("[", "")
    arr = arr.replace("]", "")

    if not arr:
        if 'R' in func:
            print("[]")
        else:
            print("error")
        continue

    arr = deque(map(int, arr.split(",")))

    rev_flag = False
    flag = True
    for char in func:
        if char == 'R':
            rev_flag = not rev_flag
        elif arr and char == 'D':
            if rev_flag:
                arr.pop()
            else:
                arr.popleft()
        else:
            flag = False
            break

    if flag:
        result = "["
        if rev_flag:
            arr.reverse()
            result += ",".join(map(str, arr))
        else:
            result += ",".join(map(str, arr))
        result += "]"
        print(result)
    else:
        print("error")
