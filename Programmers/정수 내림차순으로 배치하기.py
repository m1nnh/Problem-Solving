"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 정수 내림차순으로 배치하기
description : 조인
"""


def solution(n):
    list_n = str(n)
    sort_number = sorted(list_n, reverse=True)
    answer = "".join(sort_number)
    return int(answer)
