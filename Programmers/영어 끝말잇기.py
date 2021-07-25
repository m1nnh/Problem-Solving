"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 영어 끝말잇기
description : 딕셔너리
"""


def solution(n, words):
    answer = []

    total_count = 1
    index = 2

    dic = {}

    dic[words[0]] = 1
    last = words[0][-1]
    flag = True

    for i in range(1, len(words)):
        if last == words[i][0]:
            if words[i] not in dic:
                dic[words[i]] = 1
                last = words[i][-1]
                if index == n:
                    index = 1
                    total_count += 1
                else:
                    index += 1
            else:
                flag = False
                break
        else:
            flag = False
            break

    if flag:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(index)
        answer.append(total_count)

    return answer
