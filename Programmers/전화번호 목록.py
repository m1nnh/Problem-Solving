"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 전화번호 목록
description : 해시
"""


def solution(phone_book):
    answer = True
    dic = {}
    for phone_num in phone_book:
        dic[phone_num] = 1

    for phone_num in phone_book:
        result = ""
        for i in range(len(phone_num) - 1):
            result += phone_num[i]
            if result in dic:
                answer = False
                break
        if answer is False:
            break
    return answer
