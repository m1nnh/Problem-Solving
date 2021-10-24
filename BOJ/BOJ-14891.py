"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 톱니바퀴
description : 구현
"""

from collections import deque


def rotate(gear_wheel_number, direction):
    global gear_wheels

    if direction == 1:
        last = gear_wheels[gear_wheel_number].pop()
        gear_wheels[gear_wheel_number].appendleft(last)
    else:
        first = gear_wheels[gear_wheel_number].popleft()
        gear_wheels[gear_wheel_number].append(first)


def solution(gear_wheel_number, direction):
    global gear_wheels
    now = direction
    flag = [0, 0, 0, 0]
    flag[gear_wheel_number] = direction

    if gear_wheel_number == 0:
        for i in range(1, len(gear_wheels)):
            if gear_wheels[i - 1][2] != gear_wheels[i][6]:
                flag[i] = flag[i - 1] * (-1)
            else:
                break
    elif gear_wheel_number == 3:
        for i in range(gear_wheel_number - 1, -1, -1):
            if gear_wheels[i][2] != gear_wheels[i + 1][6]:
                flag[i] = flag[i + 1] * (-1)
            else:
                break
    else:
        for i in range(gear_wheel_number + 1, len(gear_wheels)):
            if gear_wheels[i - 1][2] != gear_wheels[i][6]:
                flag[i] = flag[i - 1] * (-1)
            else:
                break
        now = direction
        for i in range(gear_wheel_number - 1, -1, -1):
            if gear_wheels[i][2] != gear_wheels[i + 1][6]:
                flag[i] = flag[i + 1] * (-1)
            else:
                break

    for i in range(4):
        if flag[i] != 0:
            rotate(i, flag[i])


if __name__ == "__main__":
    global gear_wheels
    gear_wheels = [deque() for _ in range(4)]
    answer = 0

    for i in range(4):
        gear_wheel = list(map(int, input()))
        for j in range(len(gear_wheel)):
            gear_wheels[i].append(gear_wheel[j])

    K = int(input())

    for _ in range(K):
        gear_wheel_number, direction = map(int, input().split())
        solution(gear_wheel_number - 1, direction)

    for i in range(4):
        if gear_wheels[i][0] == 1:
            answer += 2 ** i

    print(answer)
