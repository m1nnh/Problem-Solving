"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 소수 만들기
description : 구현, 에라토스테네스 체
"""

import math

def solution(nums):
    answer = 0
    is_prime_table = is_prime_number()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if is_prime_table[nums[i] + nums[j] + nums[k]] is True:
                    answer += 1

    return answer

def is_prime_number():
    prime_table = [True] * 2998
    prime_table[0], prime_table[1] = False, False

    for i in range(2, int(math.sqrt(len(prime_table))) + 1):
        for j in range(i * 2, len(prime_table), i):
            prime_table[j] = False
    return prime_table

print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
