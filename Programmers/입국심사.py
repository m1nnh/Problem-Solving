"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 입국심사
description : 이분탐색
"""


def solution(n, times):
    left = 1
    right = n * max(times)

    while left < right:
        count = 0
        mid = (left + right) // 2

        for time in times:
            count += mid // time

        if count >= n:
            right = mid
        else:
            left = mid + 1
    answer = left
    return answer
