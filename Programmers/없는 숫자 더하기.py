"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 없는 숫자 더하기
description : 수학
"""


def solution(numbers):
    answer = 0

    for i in range(1, 10):
        if numbers.count(i) == 0:
            answer += i

    return answer
