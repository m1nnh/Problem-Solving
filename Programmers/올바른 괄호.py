"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 올바른 괄호
description : 스택
"""


def solution(s):
    answer = True

    stack = []

    for string in s:
        if string == "(":
            stack.append(string)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                answer = False
                break

    if len(stack) != 0:
        answer = False

    return answer
