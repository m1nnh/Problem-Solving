"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 가장 큰 수
description : 정렬
"""


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    sort_numbers = sorted(numbers, key=lambda x: x * 3, reverse=True)
    answer = str(int("".join(sort_numbers)))
    return answer
