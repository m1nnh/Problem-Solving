"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 다음 큰 숫자
description : 수학
"""


def solution(n):
    answer = n + 1
    bin_n = format(n, "b")
    count_n = bin_n.count("1")

    while True:
        bin_number = format(answer, "b")
        if bin_number.count("1") == count_n:
            break
        else:
            answer += 1

    return answer
