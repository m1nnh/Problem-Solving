"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 행렬의 덧셈
description : 행렬
"""


def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        list = []
        for x, y in zip(i, j):
            list.append(x + y)
        answer.append(list)
    return answer
