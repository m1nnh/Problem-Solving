"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 하노이 탑 이동 순서
description : 재귀
"""

def solution(N, start, end):
    if N == 1:
        print(start, end)
        return

    solution(N - 1, start, 6 - start - end)
    print(start, end)
    solution(N - 1, 6 - start - end, end)

if __name__ == "__main__":
    N = int(input())
    print(2 ** N - 1)
    solution(N, 1, 3)
