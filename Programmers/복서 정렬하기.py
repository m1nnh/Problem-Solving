"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 복서 정렬하기
description : 정렬
"""


def solution(weights, head2head):
    info = []

    for i in range(len(head2head)):
        win_count = 0
        weight_count = 0
        n_count = 0

        for j in range(len(head2head[i])):
            if head2head[i][j] == "W":
                win_count += 1
                if weights[i] < weights[j]:
                    weight_count += 1
            elif head2head[i][j] == "N":
                n_count += 1

        if len(weights) - n_count != 0:
            info.append([(win_count / (len(weights) - n_count)) * 100, weight_count, weights[i], i])
        else:
            info.append([0, weight_count, weights[i], i])

    info.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))

    answer = [info[i][3] + 1 for i in range(len(info))]

    return answer
