"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 수 정렬하기 3
description : 정렬
"""

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
dic = defaultdict(int)

for i in range(N):
    dic[int(input())] += 1

dic = sorted(dic.items())

for i in range(len(dic)):
    for j in range(dic[i][1]):
        print(dic[i][0])
