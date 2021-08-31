"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 110 옮기기
description : 스택
"""


def temp_number(bin_number, n):
    point = list("110")
    stack = []

    for i in range(n):
        stack.append(bin_number[i])
        if stack[-3:] == point:
            stack.pop()
            stack.pop()
            stack.pop()

    count = int((n - len(stack)) / 3)

    for i in range(len(stack) + 1):
        temp = (stack[i: i + 3] * 3)[: 3]
        if temp > point:
            break

    return "".join(stack[: i] + point * count + stack[i:])


def solution(s):
    answer = []

    for bin_number in s:
        answer.append(temp_number(bin_number, len(bin_number)))

    return answer
