"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 나누어 떨어지는 숫자 배열
description : 구현, 수학
"""


def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]

    if not answer:
        answer.append(-1)
    else:
        answer.sort()

    return answer


if __name__ == '__main__':
    print(solution([5, 9, 7, 10], 5))
    print(solution([2, 36, 1, 3], 1))
    print(solution([3, 2, 6], 10))
