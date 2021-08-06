"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 행렬의 곱셈
description : 수학
"""


def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        array = []
        for j in range(len(arr2[0])):
            result = 0
            for k in range(len(arr1[0])):
                result += arr1[i][k] * arr2[k][j]
            array.append(result)
        answer.append(array)

    return answer
