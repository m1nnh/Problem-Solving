"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 수 정렬하기 2
description : 정렬
"""

import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

[print(x) for x in arr]
