"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 삼진법 뒤집
description : 수학
"""

import math


def solution(n):
    answer = 0
    length = 0
    if n < 3:
        answer = n
        return answer
    else:
        length = int(math.log(n, 3))

    while n >= 3:
        answer += (n % 3) * (3 ** length)
        length -= 1
        n //= 3

    answer += n

    return answer


if __name__ == '__main__':
    print(solution(45))
    print(solution(229))
