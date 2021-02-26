"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 퀵 정렬
"""


def quick_sort(array):
    if len(array) <= 1:
        return

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x < pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + quick_sort(right_side)


array = list(map(int, input().split()))

print(quick_sort(array))
