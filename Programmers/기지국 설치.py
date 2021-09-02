"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 기지국 설치
description : 수학
"""


def solution(n, stations, w):
    answer = 0
    last = 1

    for i in range(len(stations)):
        now = stations[i] - w
        if now != last and now > 1:
            if (now - last) // ((w * 2) + 1) == 0:
                answer += 1
            elif (now - last) % ((w * 2) + 1) == 0:
                answer += (now - last) // ((w * 2) + 1)
            else:
                answer += (now - last) // ((w * 2) + 1) + 1

        last = stations[i] + w + 1

        if i == len(stations) - 1:
            last -= 1
            if last < n:
                if (n - last) // ((w * 2) + 1) == 0:
                    answer += 1
                elif (n - last) % ((w * 2) + 1) == 0:
                    answer += (n - last) // ((w * 2) + 1)
                else:
                    answer += (n - last) // ((w * 2) + 1) + 1

    return answer
