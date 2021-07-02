"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 약수의 개수와 덧셈
description : 구현
"""


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        result = counted(i)
        if result % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer


def counted(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
        else:
            continue
    return count
