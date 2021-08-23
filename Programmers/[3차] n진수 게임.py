"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [3차] n진수 게임
description : 구현, 진법 변환
"""


def solution(n, t, m, p):
    answer = ''
    count = 2
    total = 0
    number = 1

    if p == 1:
        answer += "0"
        total += 1

    while total < t:
        temp_number = ""
        temp_num = number

        while temp_num != 0:
            if temp_num % n < 10:
                temp_number += str(temp_num % n)
            else:
                temp_number += chr(ord("A") + ((temp_num % n) % 10))
            temp_num //= n

        reverse_number = temp_number[::-1]

        for string_number in reverse_number:

            if count > m:
                count = 1
            if count == p and total < t:
                answer += string_number
                total += 1
                count += 1
            else:
                count += 1

        number += 1

    return answer
