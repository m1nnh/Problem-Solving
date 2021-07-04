"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [1차] 다트게임
description : 시뮬레이션
"""

from collections import deque


def solution(dartResult):
    answer = 0
    result = deque()
    number = ''
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            number += dartResult[i]
        elif dartResult[i].isalpha():
            now = int(number)
            if dartResult[i] == 'D':
                now **= 2
            elif dartResult[i] == 'T':
                now **= 3
            result.append(int(now))
            number = ''
        else:
            if dartResult[i] == '*':
                if len(result) == 1:
                    result[0] *= 2
                else:
                    result[-1] *= 2
                    result[-2] *= 2
            else:
                result[-1] *= (-1)

    answer = sum(result)

    return answer
