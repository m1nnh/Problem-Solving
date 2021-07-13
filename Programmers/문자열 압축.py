"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 압축
description : 슬라이싱
"""


def solution(s):
    answer = len(s)
    for i in range(1, len(s) - 1):
        string = s[0: i]
        result = ""
        count = 1
        for j in range(i, len(s) + i, i):

            if s[j - i: j] == s[j: j + i]:
                count += 1
            else:
                if count != 1:
                    result += str(count) + string
                else:
                    result += string
                count = 1
                string = s[j: j + i]

        if count != 1:
            result += str(count) + string
        answer = min(answer, len(result))

    return answer
