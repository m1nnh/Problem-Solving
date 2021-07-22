"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 주식 가격
description :
"""

def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i, len(prices)):
            if j == i :
                continue
            elif prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    return answer