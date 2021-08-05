"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최댓값과 최솟값
description : 수학
"""


def solution(s):
    num_list = list(map(int, s.split()))
    answer = str(min(num_list)) + " " + str(max(num_list))
    return answer
