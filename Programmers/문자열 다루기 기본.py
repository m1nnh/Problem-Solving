"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 다루기 기본
description : 구현
"""


def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for string in s:
            if string.isalpha():
                answer = False
                break
    else:
        answer = False
    return answer
