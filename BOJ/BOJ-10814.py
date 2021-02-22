"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 나이순 정렬
description :
"""

import sys

N = int(sys.stdin.readline())

Member = []

for i in range(N):
    Info = list(map(str, sys.stdin.readline().split()))
    Member.append(Info)

Member.sort(key= lambda x: (int(x[0])))

[print(' '.join(x)) for x in Member]


