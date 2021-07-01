"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 로또의 최고 순위와 최저 순위
description : 구현
"""


def solution(lottos, win_nums):
    answer = []
    zero_count = 0
    success_count = 0
    for number in lottos:
        if number == 0:
            zero_count += 1
            continue
        else:
            if number in win_nums:
                success_count += 1
            else:
                continue

    if zero_count == 0:
        if success_count == 0:
            answer.append(6)
            answer.append(6)
        else:
            answer.append(7 - success_count)
            answer.append(7 - success_count)
    else:
        if zero_count == 6:
            answer.append(1)
            answer.append(6)
        else:
            answer.append(7 - success_count - zero_count)
            answer.append(7 - success_count)
    return answer
