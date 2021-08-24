"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 부족한 금액 계산하기
description : 수학
"""


def solution(price, money, count):
    answer = 0
    original_price = price

    for i in range(count):
        money -= price
        price += original_price

    if money < 0:
        answer = money * (-1)

    return answer