"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 자연수 뒤집어 배열로 만들기
description : 문자열
"""


def solution(n):
    string = str(n)
    string = string[::-1]
    answer = [int(number) for number in string]

    return answer
