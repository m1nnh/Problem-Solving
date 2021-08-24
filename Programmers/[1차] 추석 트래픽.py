"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [1차] 추석 트래픽
description : 구현, 수학
"""


def solution(lines):
    answer = 1

    if len(lines) == 1:
        return answer

    times = []

    for line in lines:
        split_line = line.split()
        end_time = list(map(float, split_line[1].split(":")))
        time = int((3600000 * end_time[0]) + (60000 * end_time[1]) + (end_time[2] * 1000))

        if time == 0.0:
            times.append([0, 1])
            times.append([0, -1])
        else:
            times.append([time, -1])
            times.append([time - int(float(split_line[-1][:-1]) * 1000) + 1, 1])

    times.sort(key=lambda x: x[0])
    temp = 0

    for i in range(len(times)):
        count = temp

        for time in times[i:]:

            if time[0] - times[i][0] > 999:
                break
            if time[1] > 0:
                count += 1

        answer = max(answer, count)
        temp += times[i][1]

    return answer
