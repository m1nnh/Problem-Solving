"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 이진 변환 반복하기
description : 그리디
"""


def solution(s):
    answer = [0, 0]

    while len(s) != 1:
        result = ""

        for i in range(len(s)):
            if s[i] == "1":
                result += s[i]
            else:
                answer[1] += 1

        number = len(result)
        s = format(number, "b")

        answer[0] += 1

    return answer
