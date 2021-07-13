"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 오픈채팅방
description : 딕셔너리, 파싱
"""


def solution(record):
    answer = []
    result = []
    dic = {}

    for string in record:
        array = string.split()

        if array[0] in ["Enter", "Change"]:
            dic[array[1]] = array[2]

        result.append([array[0], array[1]])

    for i in range(len(result)):
        if result[i][0] == "Enter":
            answer.append(dic[result[i][1]] + "님이 들어왔습니다.")
        elif result[i][0] == "Leave":
            answer.append(dic[result[i][1]] + "님이 나갔습니다.")
    return answer
