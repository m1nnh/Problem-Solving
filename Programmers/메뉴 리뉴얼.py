"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 메뉴 리뉴얼
description : 구현
"""

from itertools import combinations


def solution(orders, course):
    answer = []
    str_orders = []
    length = [0] * 11
    result = {}
    dic = {}

    for string in orders:
        str_orders.append(list(map(str, string)))

    for order in str_orders:
        order.sort()
        for i in range(1, len(order)):
            comb = list(combinations(order, i + 1))
            for cb in comb:
                if cb not in dic:
                    dic[cb] = 1
                else:
                    dic[cb] += 1

    for key, value in dic.items():
        string = ""
        for i in key:
            string += i
        result[string] = value
        if value != 1:
            length[len(string)] = max(length[len(string)], value)

    for key, value in result.items():
        if value == length[len(key)] and len(key) in course:
            answer.append(key)
    answer = sorted(answer)

    return answer
