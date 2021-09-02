"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 풍선 터트리기
description : 이진 탐색
"""


def solution(a):
    answer = 2

    if 0 < len(a) <= 2:
        return len(a)

    left, right = a[0], a[-1]

    for i in range(1, len(a) - 1):
        if left > a[i]:
            answer += 1
            left = a[i]
        if right > a[-1 - i]:
            answer += 1
            right = a[-1 - i]

    if left == right:
        answer -= 1

    return answer
