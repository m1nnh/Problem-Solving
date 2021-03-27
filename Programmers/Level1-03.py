"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 완주하지 못한 선수
description : 딕셔너리
"""


def solution(participant, completion):
    answer = ''
    dic = {}
    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in completion:
        dic[i] -= 1

    for i, j in dic.items():
        if j == 1:
            answer = i
            break

    return answer
