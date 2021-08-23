"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [3차] 방금그곡
description : 구현
"""


def check(musicinfos):
    infos = []

    for music_info in musicinfos:
        mi = list(map(str, music_info.split(",")))

        start, end = list(map(int, mi[0].split(":"))), list(map(int, mi[1].split(":")))

        index, code, time = 0, "", 0

        while start[0] != end[0] or start[1] != end[1]:
            if index >= len(mi[-1]):
                index = 0

            now_code = mi[-1][index]

            if index + 1 < len(mi[-1]):
                if mi[-1][index + 1] == "#":
                    now_code += mi[-1][index + 1]
                    index += 1

            index += 1
            code += now_code
            start[1] += 1
            time += 1

            if start[1] == 60:
                start[0] += 1
                start[1] = 0

        infos.append([time, code, mi[2]])

    return infos


def solution(m, musicinfos):

    answer = ""
    infos = check(musicinfos)
    result = []

    for info in infos:
        flag = False

        for i in range(len(info[1]) - len(m) + 1):

            if info[1][i: len(m) + i] == m:
                if len(m) + i < len(info[1]):
                    if info[1][len(m) + i] != "#":
                        flag = True
                        break
                else:
                    flag = True
                    break

        if flag:
            if len(result) == 0:
                result.append([info[0], info[2]])
            elif result[0][0] < info[0]:
                result[0][0], result[0][1] = info[0], info[2]

    if len(result) == 0:
        answer += "(None)"
    else:
        answer += result[0][-1]

    return answer