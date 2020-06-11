"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 소수 구하기
description : 수학, 정수론, 소수판정, 에라토스테네스의 체
"""
import math
import sys

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n + 1):
    if i == 1:
        continue
    flag = True
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            flag = False
            break
    if flag is True:
        print(i)
