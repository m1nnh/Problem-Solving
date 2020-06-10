"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 프린터 큐
description : 구현, 자료구조, 시뮬레이션, 큐
"""

from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    paper = deque()
    imp = list(map(int, input().split()))

    for j in range(len(imp)):
        paper.append([j, imp[j]])

    count = 0
    while paper:
        idx, pri = paper.popleft()
        flag = True
        for k in paper:
            if k[1] > pri:
                flag = False
                break

        if flag is True:
            count += 1
            if idx == m:
                print(count)
                break
        else:
            paper.append([idx, pri])
