"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 국영수
description : 정렬
"""

import sys

input = sys.stdin.readline

N = int(input())
students = []

for i in range(N):
    students.append(input().split())

result = sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

[print(result[i][0]) for i in range(N)]
