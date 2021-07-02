"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [1차] 비밀지도
description : 구현
"""


def solution(n, arr1, arr2):
    answer = []
    str1 = ''
    str2 = ''
    for i in range(n):
        test1 = ''
        test2 = ''
        for _ in range(n):
            test1 += str(arr1[i] % 2)
            arr1[i] //= 2
            test2 += str(arr2[i] % 2)
            arr2[i] //= 2
        str1 += test1[:: -1]
        str2 += test2[:: -1]

    result = ''

    if str1[0] == '0' and str2[0] == '0':
        result += ' '
    else:
        result += '#'

    for i in range(1, len(str1)):
        if i % n == 0:
            if i == len(str1) - 1:
                break
            answer.append(result)
            result = ''
        if str1[i] == '0' and str2[i] == '0':
            result += ' '
        else:
            result += '#'

    answer.append(result)
    return answer
