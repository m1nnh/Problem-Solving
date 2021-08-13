"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 베스트앨범
description : 해시, 정렬
"""

from collections import defaultdict


def solution(genres, plays):
    dic = defaultdict(list)
    total_dic = defaultdict(int)
    index = 0
    answer = []

    for genre, play in zip(genres, plays):
        dic[genre].append([play, index])
        total_dic[genre] += play
        index += 1
    for key, value in dic.items():
        dic[key] = sorted(value, key=lambda x: (-x[0], x[1]))

    sort_dic = sorted(total_dic.items(), key=lambda x: -x[1])

    for i in range(len(sort_dic)):
        for j in range(2):
            if len(dic[sort_dic[i][0]]) != 0:
                values = dic[sort_dic[i][0]].pop(0)
                answer.append(values[1])

    return answer
