"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 재귀함수를 이용한 이진탐색
description :

"""


def binary_search(array, start, end, M):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] < M:
        return binary_search(array, mid + 1, end, M)
    elif array[mid] > M:
        return binary_search(array, start, mid - 1, M)
    else:
        return mid


N, M = map(int, input().split())

array = list(map(int, input().split()))

result = binary_search(array, 0, N - 1, M)

if result == None:
    print('none')
else:
    print(result + 1)
