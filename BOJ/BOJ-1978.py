"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 소수 찾기
description : 수학, 정수론, 소수 판정, 에라토스테네스의 체
"""

import math

n = int(input())
num_list = list(map(int, input().split()))
prime_number = [True for _ in range(max(num_list) + 1)]
prime_number[0], prime_number[1] = False, False

for i in range(2, int(math.sqrt(max(num_list))) + 1):
    for j in range(i * 2, max(num_list) + 1, i):
        prime_number[j] = False

count = 0

for i in range(len(num_list)):
    if prime_number[num_list[i]] is True:
        count += 1
print(count)
