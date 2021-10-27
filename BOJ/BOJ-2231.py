"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 분해합
description : 브루트포스 알고리즘
"""

def solution(N):
    answer = 0

    for i in range(1, N + 1):
        temp_list = list(map(int, str(i)))
        if sum(temp_list) + i == N:
            answer = i
            break

    return answer


if __name__ == "__main__":
    N = int(input())
    print(solution(N))
