"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [3차] 압축
description : 시뮬레이션, 구현, 해시, 슬라이싱
"""

from collections import defaultdict


def solution(msg):
    answer = []
    dic = defaultdict(int)

    for i in range(0, 26):
        dic[chr(ord('A') + i)] = i + 1

    count = 27
    index = 0

    while index <= len(msg) - 1:

        message = msg[index]
        slice_index = 1

        for i in range(index + 1, len(msg)):
            message += msg[i]

            if message not in dic:
                dic[message] = count
                count += 1
                break

            else:
                index += 1
                slice_index += 1
                continue

        answer.append(dic[message[0: slice_index]])
        index += 1

    return answer
