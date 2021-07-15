"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 튜플
description : 문자열
"""


def solution(s):
    result = ""
    dic = {}

    for string in s:
        if string in ["}", ","]:
            if len(result) != 0:
                if int(result) not in dic:
                    dic[int(result)] = 1
                else:
                    dic[int(result)] += 1
                result = ""
        elif string.isdigit():
            result += string
        else:
            continue

    answer = sorted(dic, key=lambda x: -dic[x])

    return answer
