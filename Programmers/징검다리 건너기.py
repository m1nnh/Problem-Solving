"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 징검다리 건너기
description : 이진 탐색
"""


def solution(stones, k):
    left, right = 1, max(stones)
    answer = 1

    while left <= right:
        mid = (left + right) // 2
        count = 0
        flag = True

        for stone in stones:
            if stone < mid:
                count += 1

                if count == k:
                    flag = False
                    break
            else:
                count = 0

        if flag is True:
            answer = max(answer, mid)
            left = mid + 1

        else:
            right = mid - 1

    return answer
