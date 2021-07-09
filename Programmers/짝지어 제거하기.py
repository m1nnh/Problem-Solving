"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 짝지어 제거하기
description : 스택
"""


def solution(s):
    if len(s) % 2 != 0:
        return 0

    answer = 1
    stack = []

    for string in s:
        if len(stack) == 0:
            stack.append(string)
        else:
            if stack[-1] == string:
                stack.pop()
            else:
                stack.append(string)

    if stack:
        answer = 0

    return answer
