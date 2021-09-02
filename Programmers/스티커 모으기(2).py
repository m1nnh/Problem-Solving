"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 스티커 모으기 (2)
description : 다이나믹 프로그래밍
"""


def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    dp1 = [0 for _ in range(len(sticker))]
    dp2 = [0 for _ in range(len(sticker))]

    dp1[0], dp1[1] = sticker[0], sticker[0]
    dp2[0], dp2[1] = 0, sticker[1]

    for i in range(2, len(sticker)):
        if i == len(sticker) - 1:
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])
            break
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    answer = max(max(dp1), max(dp2))

    return answer
