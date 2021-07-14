"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 조이스틱
description : 그리디
"""


def solution(name):
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0
    answer = 0
    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0:
            break
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right

    return answer
