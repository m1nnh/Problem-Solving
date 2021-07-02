"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 음양 더하기
description : 수학
"""


def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] is False:
            answer -= absolutes[i]
        else:
            answer += absolutes[i]
    return answer
