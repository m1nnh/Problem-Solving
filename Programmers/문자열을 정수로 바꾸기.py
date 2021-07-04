"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열을 정수로 바꾸기
description : 문자열
"""


def solution(s):
    answer = 0
    if s[0] == '-':
        answer = (-1) * int(s[1:])
    else:
        answer = int(s)
    return answer
