"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 연산자 끼워넣기
description : 구현
"""

import sys

sys.setrecursionlimit(10 ** 6)

operation = ["+", "-", "*", "/"]


def solution(N, numbers, operation_count, operations):
    global max_value, min_value

    if len(operations) == N - 1:
        answer = numbers[0]
        for i in range(1, N):
            if operations[i - 1] == "+":
                answer += numbers[i]
            elif operations[i - 1] == "-":
                answer -= numbers[i]
            elif operations[i - 1] == "*":
                answer *= numbers[i]
            else:
                if answer < 0:
                    answer *= (-1)
                    answer //= numbers[i]
                    answer *= (-1)
                else:
                    answer //= numbers[i]

        max_value = max(max_value, answer)
        min_value = min(min_value, answer)
        return

    for i in range(4):
        if operation_count[i] > 0:
            operation_count[i] -= 1
            operations.append(operation[i])
            solution(N, numbers, operation_count, operations)
            operations.pop()
            operation_count[i] += 1


if __name__ == "__main__":
    global max_value, min_value
    max_value = -int(1e9)
    min_value = int(1e9)

    N = int(input())
    numbers = list(map(int, input().split()))
    operation_count = list(map(int, input().split()))

    solution(N, numbers, operation_count, [])

    print(max_value)
    print(min_value)
