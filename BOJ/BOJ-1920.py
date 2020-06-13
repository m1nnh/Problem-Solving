"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 수 찾기
description : 이분 탐색
"""

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in b:
    start, end = 0, n - 1
    flag = True
    while start <= end:
        mid = (start + end) // 2
        if a[mid] < i:
            start = mid + 1
        elif a[mid] > i:
            end = mid - 1
        else:
            print(1)
            flag = False
            break
    if flag is True:
        print(0)
