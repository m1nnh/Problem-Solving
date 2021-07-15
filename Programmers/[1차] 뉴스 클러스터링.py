"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [1차] 뉴스 클러스터링
description : 문자열
"""


def solution(str1, str2):
    answer = 0
    str1, str2 = list(map(str, str1.lower())), list(map(str, str2.lower()))
    list1 = []
    list2 = []

    for i in range(len(str1) - 1):
        result = ""
        if str1[i].isalpha() and str1[i + 1].isalpha():
            result += str1[i] + str1[i + 1]
            list1.append(result)

    for i in range(len(str2) - 1):
        result = ""
        if str2[i].isalpha() and str2[i + 1].isalpha():
            result += str2[i] + str2[i + 1]
            list2.append(result)

    if len(list1) == 0 and len(list2) == 0:
        answer = 65536
    else:
        count = 0
        for string in list1:
            if string in list2:
                count += 1
                list2.remove(string)
        answer = int(count / (len(list1) + len(list2)) * 65536)

    return answer
