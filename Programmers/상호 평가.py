"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 상호 평가
description : 수학
"""


def grade(n, score):
    if score // n >= 90:
        return "A"
    elif score // n >= 80:
        return "B"
    elif score // n >= 70:
        return "C"
    elif score // n >= 50:
        return "D"
    else:
        return "F"


def solution(scores):
    answer = ''
    pre_scores = [i for i in zip(*scores)]

    index = 0

    for score in pre_scores:
        if score[index] == max(score) or score[index] == min(score):
            if score.count(score[index]) == 1:
                answer += grade(len(score) - 1, sum(score) - score[index])
            else:
                answer += grade(len(score), sum(score))
        else:
            answer += grade(len(score), sum(score))

        index += 1

    return answer