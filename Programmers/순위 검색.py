"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 순위 검색
description : 조합, 이진 탐색
"""

from bisect import bisect_left
from itertools import combinations


def make_comb(split_information):
    comb = []

    for i in range(5):
        for cb in combinations([0, 1, 2, 3], i):
            temp = ""
            for j in range(4):
                if j not in cb:
                    temp += split_information[j]
                else:
                    temp += "-"
            comb.append(temp)
    return comb


def solution(info, query):
    answer = []
    dic = {}

    for information in info:
        split_info = information.split(" ")
        comb_info = make_comb(split_info)
        for ci in comb_info:
            if ci not in dic:
                dic[ci] = [int(split_info[4])]
            else:
                dic[ci].append(int(split_info[4]))

    for key in dic.keys():
        dic[key].sort()

    for qry in query:
        split_query = qry.split(" ")
        result = split_query[0] + split_query[2] + split_query[4] + split_query[6]
        if result in dic:
            answer.append(len(dic[result]) - bisect_left(dic[result], int(split_query[7]), lo=0, hi=len(dic[result])))
        else:
            answer.append(0)
    return answer
