"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 시험 감독
description : 구현
"""


def solution(N, test_room, B, C):
    answer = 0

    for i in range(N):
        answer += 1
        test_room[i] -= B

        if test_room[i] <= 0:
            continue
        elif test_room[i] % C != 0:
            answer += (test_room[i] // C) + 1
        else:
            answer += test_room[i] // C

    return answer


if __name__ == "__main__":
    N = int(input())
    test_room = list(map(int, input().split()))
    B, C = map(int, input().split())

    print(solution(N, test_room, B, C))
