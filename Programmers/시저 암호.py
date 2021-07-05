"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 시저 암호
description : 아스키코드
"""


def solution(s, n):
    answer = ""
    for string in s:
        if string == " ":
            answer += string
        elif 65 <= ord(string) <= 90:
            if ord(string) + n > 90:
                answer += chr(ord(string) + n - 91 + 65)
            else:
                answer += chr(ord(string) + n)
        elif 97 <= ord(string) <= 122:
            if ord(string) + n > 122:
                answer += chr(ord(string) + n - 123 + 97)
            else:
                answer += chr(ord(string) + n)
    return answer
