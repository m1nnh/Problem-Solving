"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 퀵정렬
description : 정렬
"""


def quick_sort(array):
    if len(array) <= 1:
        return array

    tail = array[1:]
    pivot = array[0]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x >= pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print(quick_sort(array))
