"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 부품찾기
description : 이진탐색

"""


def binary_search(A, B, start, end):
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == B:
            return True
        elif A[mid] > B:
            end = mid - 1
        else:
            start = mid + 1
    return False


N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for i in B:
    result = binary_search(A, i, 0, N - 1)
    if result is True:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        
