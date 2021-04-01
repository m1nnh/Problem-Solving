"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 두 개 뽑아서 더하기
description : 투포인터
"""


def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            result = numbers[i] + numbers[j]
            if result in answer:
                continue
            else:
                answer.append(result)
    answer.sort()
    return answer
