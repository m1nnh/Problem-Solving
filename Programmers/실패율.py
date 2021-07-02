"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 실패율
description : 구현
"""


def solution(N, stages):
    answer = []
    dic = {}
    count = 0

    for i in stages:
        if i > N:
            count += 1
        elif i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    sort_dic = sorted(dic.items())
    length = len(stages)
    result = []

    for i in range(len(sort_dic)):
        result.append([sort_dic[i][0], float(sort_dic[i][1] / length)])
        length -= sort_dic[i][1]
    result = sorted(result, key=lambda x: (-x[1], x[0]))

    for i in range(len(result)):
        answer.append(result[i][0])

    if len(answer) != N:
        for i in range(1, N + 1):
            if i not in answer:
                answer.append(i)
            else:
                continue

    return answer
