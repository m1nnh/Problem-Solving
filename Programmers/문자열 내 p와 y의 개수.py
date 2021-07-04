"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 내 p와 y의 개수
description : 구현
"""


def solution(s):
    count = [0, 0]

    for string in s:
        if string == 'p' or string == 'P':
            count[0] += 1
        elif string == 'y' or string == 'Y':
            count[1] += 1

    if count[0] == count[1]:
        return True
    else:
        return False
