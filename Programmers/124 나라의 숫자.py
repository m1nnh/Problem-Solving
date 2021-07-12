"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 124 나라의 숫자
description : 수학
"""


def solution(n):
    answer = ''
    if n < 3:
        answer += str(n)
        return answer

    while n >= 3:
        decTo124 = n % 3

        if decTo124 == 0:
            n -= 1
            answer += "4"
        elif decTo124 == 1:
            answer += "1"
        else:
            answer += "2"
        n //= 3
    if n != 0:
        answer += str(n)
    answer = answer[::-1]
    return answer
