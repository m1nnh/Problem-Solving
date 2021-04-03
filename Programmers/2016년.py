"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 2016년
description : 수학
"""


def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return answer[(sum(months[: a - 1]) + b - 1) % 7]


if __name__ == '__main__':
    print(solution(5, 24))
