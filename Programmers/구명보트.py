"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 구명보트
description : 그리디
"""


def solution(people, limit):
    answer = 0
    sort_people = sorted(people)
    left, right = 0, len(sort_people) - 1

    while left <= right:
        answer += 1
        if sort_people[left] + sort_people[right] <= limit:
            left += 1
        right -= 1

    return answer
