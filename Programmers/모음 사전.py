"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 모음 사전
description : 수학
"""


def solution(word):
    answer = 0
    word_dic = {"E": 1, "I": 2, "O": 3, "U": 4}

    for i in range(len(word)):
        if word[i] == "A":
            answer += 1
        else:
            for j in range(4, i, -1):
                answer += (5 ** (j - i)) * word_dic[word[i]]
            answer += word_dic[word[i]] + 1

    return answer
