"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : LCS
description : 다이나믹프로그래밍
"""


def solution(str1, str2):
    answer = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                answer[i][j] = answer[i - 1][j - 1] + 1
            else:
                answer[i][j] = max(answer[i][j - 1], answer[i - 1][j])

    return answer[-1][-1]


if __name__ == "__main__":
    str1 = input()
    str2 = input()

    print(solution(str1, str2))
