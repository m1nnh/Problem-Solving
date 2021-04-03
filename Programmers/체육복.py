"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 체육복
description : 그리디 알고리즘
"""


def solution(n, lost, reserve):
    students = [1] * (n + 1)
    students[0] = -1

    for i in reserve:
        students[i] += 1

    for i in lost:
        students[i] -= 1

    for i in range(1, len(students)):
        if students[i] == 2:
            if students[i - 1] == 0:
                students[i] -= 1
                students[i - 1] += 1
                continue

            if i + 1 < len(students) and students[i + 1] == 0:
                students[i] -= 1
                students[i + 1] += 1

    answer = [x for x in students if x > 0]

    return len(answer)


if __name__ == '__main__':
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
