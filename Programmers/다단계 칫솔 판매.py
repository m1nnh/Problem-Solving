"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 다단계 칫솔 판매
description : 구현
"""

from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    dic = defaultdict(list)

    for i in range(len(enroll)):
        dic[enroll[i]].append([referral[i], 0])

    for i in range(len(seller)):
        price = 100 * amount[i]
        tip = price // 10
        dic[seller[i]][0][1] += (price - tip)

        if dic[seller[i]][0][0] != "-":
            now = dic[seller[i]][0][0]

            while True and tip != 0:
                dic[now][0][1] += (tip - (tip // 10))
                now = dic[now][0][0]
                tip //= 10

                if now == "-":
                    break
        else:
            continue

    for member in enroll:
        answer.append(dic[member][0][1])

    return answer
