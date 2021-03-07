"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 떡볶이 떡 만들기
description : 이진탐색

"""


def binary_search(array, start, end, M):
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in array:
            if i // mid == 0:
                continue
            else:
                count += (i % mid)
        if count == M:
            return mid
        elif count > M:
            start = mid + 1
        else:
            end = mid - 1


N, M = map(int, input().split())
array = list(map(int, input().split()))

print(binary_search(array, 0, max(array), M))
