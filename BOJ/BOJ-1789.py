"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Sum numbers
description : Binary search
"""

N = int(input())
i = 1
num_sum = 0

while num_sum <= N:
    num_sum += i
    i += 1

print(i - 2)
