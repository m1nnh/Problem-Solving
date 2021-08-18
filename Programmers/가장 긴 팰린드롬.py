"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 가장 긴 팰린드롬
description : 완전 탐색
"""


def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i: j] == s[i: j][::-1]:
                answer = max(answer, len(s[i: j]))
    return answer
