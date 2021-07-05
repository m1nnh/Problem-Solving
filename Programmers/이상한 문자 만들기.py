"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 이상한 문자 만들기
description : 문자열
"""


def solution(s):
    answer = ""
    count = 0
    for string in s:
        if string == " ":
            answer += string
            count = 0
            continue
        elif count % 2 == 0:
            answer += string.upper()
        else:
            answer += string.lower()
        count += 1

    return answer
