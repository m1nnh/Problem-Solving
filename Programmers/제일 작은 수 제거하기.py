"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 제일 작은 수 제거하기
description : 수학
"""


def solution(arr):
    arr.remove(min(arr))
    answer = arr

    if len(answer) == 0:
        answer.append(-1)

    return answer
