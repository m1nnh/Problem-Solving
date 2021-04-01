"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 같은 숫자는 싫어
description : 구현
"""


def solution(arr):
    answer = []
    for num in arr:
        if not answer or answer[-1] != num:
            answer.append(num)

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 3, 3, 0, 1, 1]))
    print(solution([4, 4, 4, 3, 3]))
