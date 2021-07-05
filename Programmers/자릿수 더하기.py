"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 자릿수 더하기
description : 문자열
"""


def solution(n):
    answer = 0
    string = str(n)
    for number in string:
        answer += int(number)

    return answer
