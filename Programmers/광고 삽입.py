"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 광고 삽입
description : 구현
"""


def str_to_int(time):
    h, m, s = time.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    result = ""
    if 10 > time // 3600:
        result += "0" + str(time // 3600) + ":"
    else:
        result += str(time // 3600) + ":"

    time %= 3600

    if 10 > time // 60:
        result += "0" + str(time // 60) + ":"
    else:
        result += str(time // 60) + ":"

    time %= 60

    if 10 > time:
        result += "0" + str(time)
    else:
        result += str(time)

    return result


def solution(play_time, adv_time, logs):
    answer = ''
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    print(play_time)
    if play_time == adv_time:
        return "00:00:00"

    user_log = [0 for i in range(play_time + 1)]

    for log in logs:
        start, end = log.split("-")
        start_log = str_to_int(start)
        end_log = str_to_int(end)

        user_log[start_log] += 1
        user_log[end_log] -= 1

    for i in range(1, len(user_log)):
        user_log[i] = user_log[i] + user_log[i - 1]

    for i in range(1, len(user_log)):
        user_log[i] = user_log[i] + user_log[i - 1]

    max_view = 0
    max_time = 0

    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if max_view < user_log[i] - user_log[i - adv_time]:
                max_view = user_log[i] - user_log[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if max_view < user_log[i]:
                max_view = user_log[i]
                max_time = i - adv_time + 1

    answer = int_to_str(max_time)
    return answer
