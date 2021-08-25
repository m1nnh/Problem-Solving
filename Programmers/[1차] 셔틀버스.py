"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [1차] 셔틀버스
description : 구현
"""


def solution(n, t, m, timetable):
    answer = ''
    times = []

    for time in timetable:
        split_time = time.split(":")
        times.append((60 * int(split_time[0])) + int(split_time[1]))

    times.sort()
    bus = [[] for _ in range(n)]
    time = 540

    for i in range(n):

        while True:
            if len(bus[i]) == m or len(times) == 0:
                break
            if time >= times[0]:
                bus[i].append(times.pop(0))
            else:
                break

        time += t

    time -= t

    if len(bus[-1]) == m:
        time = bus[-1][-1] - 1

    if time // 60 < 10:
        answer += "0" + str(time // 60) + ":"
    else:
        answer += str(time // 60) + ":"

    if time % 60 < 10:
        answer += "0" + str(time % 60)
    else:
        answer += str(time % 60)

    return answer
