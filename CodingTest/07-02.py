"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 이진 탐색(재귀)
"""


def binary_search(arr, start, end, s):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == s:
        return mid
    elif array[mid] > s:
        return binary_search(arr, start, mid - 1, s)
    else:
        return binary_search(arr, mid + 1, end, s)


N, S = map(int, input().split())
array = list(map(int, input().split()))
index = binary_search(array, 0, len(array) - 1, S)
print(index + 1)
