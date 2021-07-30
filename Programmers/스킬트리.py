"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 스킬트리
description : 딕셔너리
"""


def solution(skill, skill_trees):
    answer = 0
    dic = {}
    count = 1
    for sk in skill:
        dic[sk] = count
        count += 1

    for skt in skill_trees:
        cnt = 1
        flag = True
        for string in skt:
            if string not in dic:
                continue
            else:
                if dic[string] == cnt:
                    cnt += 1
                else:
                    flag = False
        if flag:
            answer += 1
    return answer
