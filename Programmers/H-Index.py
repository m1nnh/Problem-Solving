"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : H-Index
description : 정렬
"""


def solution(citations):
    max_value = max(citations)
    answer = 0

    ct = [i for i in range(max_value, -1, -1)]

    for h in ct:
        high_number = 0
        for number in citations:
            if number >= h:
                high_number += 1
        if high_number >= h:
            answer = h
            break

    return answer
