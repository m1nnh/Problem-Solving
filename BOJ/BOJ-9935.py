"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 폭발
description : 구현
"""

import sys

input = sys.stdin.readline


def solution(str, explosion_str):
    last = explosion_str[-1]
    stack = []
    length = len(explosion_str)
    for s in str:
        stack.append(s)
        if s == last and ''.join(stack[-length:]) == explosion_str:
            del stack[-length:]

    answer = "".join(stack)

    if len(answer) == 0:
        return "FRULA"
    else:
        return answer


if __name__ == "__main__":
    str = input().rstrip()
    explosion_str = input().rstrip()
    print(solution(str, explosion_str))

