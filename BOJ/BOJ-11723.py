"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 집합
description : 비트마스킹
"""
import sys

input = sys.stdin.readline

M = int(input().rstrip())
S = set()

for _ in range(M):
    cal = input().rstrip()
    if cal == 'empty':
        S = set()
    elif cal == 'all':
        S = {x for x in range(1, 21)}
    else:
        cal, num = cal.split()
        if cal == 'add':
            S.add(int(num))
        elif cal == 'remove':
            if int(num) in S:
                S.remove(int(num))
            else:
                continue
        elif cal == 'check':
            if int(num) in S:
                print(1)
            else:
                print(0)
        else:
            if int(num) in S:
                S.remove(int(num))
            else:
                S.add(int(num))
