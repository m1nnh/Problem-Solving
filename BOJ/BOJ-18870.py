"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 좌표 압축
description : 정렬
"""

import sys

input = sys.stdin.readline

N = int(input())

X = list(map(int, input().split()))
format_X = list(sorted(set(X)))

dic = {value: idx for idx, value in enumerate(format_X)}

for x in X:
    print(dic[x], end=' ')
