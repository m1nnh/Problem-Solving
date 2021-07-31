"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 쿼드압축 후 개수 세기
description : 재귀
"""


def compression(x, y, n, arr):
    if n == 1:
        if arr[x][y] == 1:
            return [0, 1]
        else:
            return [1, 0]

    left_up = compression(x, y, n // 2, arr)
    right_up = compression(x, y + n // 2, n // 2, arr)
    left_down = compression(x + n // 2, y, n // 2, arr)
    right_down = compression(x + n // 2, y + n // 2, n // 2, arr)

    if left_up == right_up == left_down == right_down == [0, 1] or left_up == right_up == left_down == right_down == [1,
                                                                                                                      0]:
        return left_up
    else:
        return list(map(sum, zip(left_up, right_up, left_down, right_down)))


def solution(arr):
    answer = compression(0, 0, len(arr), arr)
    return answer
