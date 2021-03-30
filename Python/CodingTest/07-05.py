"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 부품 찾기 (이진탐색)
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로 한다.
"""


def binary_search(arr, start, end, f):
    mid = (start + end) // 2
    while start <= end:
        if arr[mid] == f:
            return True
        elif arr[mid] > f:
            return binary_search(arr, start, mid - 1, f)
        else:
            return binary_search(arr, mid + 1, end, f)
    return False


N = int(input())
array = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))
result = False
for i in find:
    result = binary_search(array, 0, len(array) - 1, i)
    if result is True:
        print('yes', end=' ')
    else:
        print('no', end=' ')
