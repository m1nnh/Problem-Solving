"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 하노이의 탑
description : 재귀
"""


def hanoi(n, start, end, sub):
    global answer

    if n == 1:
        answer.append([start, end])
        return

    hanoi(n - 1, start, sub, end)
    answer.append([start, end])
    hanoi(n - 1, sub, end, start)


def solution(n):
    global answer
    answer = []

    hanoi(n, 1, 3, 2)
    return answer
