"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 스타 수열
description : 수학
"""

from collections import Counter


def solution(a):
    answer = -1
    if len(a) == 1:
        return 0

    dic = Counter(a)

    for key, value in dic.items():
        if value * 2 < answer:
            continue

        idx, count = 0, 0

        while idx < len(a) - 1:
            if (a[idx] != key and a[idx + 1] != key) or a[idx] == a[idx + 1]:
                idx += 1
                continue

            count += 2
            idx += 2
        answer = max(answer, count)

    return answer
