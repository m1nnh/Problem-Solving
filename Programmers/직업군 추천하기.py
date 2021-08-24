"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 직업군 추천하기
description : 해시
"""

from collections import defaultdict


def solution(table, languages, preference):
    table_dic = defaultdict(list)
    company = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]

    result = []

    for tb in table:
        split_table = tb.split()
        table_dic[split_table[0]] = split_table[1:][::-1]

    for com in company:
        score = 0
        for i in range(len(languages)):
            if languages[i] in table_dic[com]:
                score += (preference[i] * (table_dic[com].index(languages[i]) + 1))
            else:
                continue
        result.append([score, com])

    sorted_result = sorted(result, key=lambda x: (-x[0], x[1]))

    answer = sorted_result[0][-1]

    return answer