"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 핸드폰 번호 가리기
description : 문자열
"""


def solution(phone_number):
    answer = ''

    for i in range(0, len(phone_number) - 4):
        answer += "*"
    for i in range(len(phone_number) - 4, len(phone_number)):
        answer += phone_number[i]

    return answer
