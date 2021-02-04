"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 예산
description : 이분탐색
"""

N = int(input())
array = list(map(int, input().split()))
M = int(input())
low, high = 0, max(array)

while low <= high:
    mid = (low + high) // 2
    sum_value = 0
    for i in array:
        if i >= mid:
            sum_value += mid
        else:
            sum_value += i
    if sum_value <= M:
        low = mid + 1
    else:
        high = mid - 1
print(high)
