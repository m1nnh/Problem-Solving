"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 반복문을 이용한 이진탐색
description : 이진탐색

"""


def binary_search(array, start, end, M):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == M:
            return mid
        elif array[mid] > M:
            end = mid - 1
        else:
            start = mid + 1
    return None


N, M = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, 0, N - 1, M)

if result is None:
    print('None')
else:
    print(result + 1)
