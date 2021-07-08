"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 숫자 문자열과 영단어
description : 딕셔너리
"""


def solution(s):
    dic = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
           "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
    result = ""
    temp = ""
    for string in s:
        if string.isdigit():
            result += string
        else:
            temp += string
            if temp in dic.keys():
                result += dic[temp]
                temp = ""
    answer = int(result)

    return answer
