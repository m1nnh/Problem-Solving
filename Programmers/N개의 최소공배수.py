"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : N개의 최소공배수
description : 완전탐색
"""


def solution(arr):
    answer = 1

    while True:
        flag = True
        for num in arr:
            if answer % num != 0:
                flag = False
                break
        if flag:
            break
        else:
            answer += 1

    return answer
