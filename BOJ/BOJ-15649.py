"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : N과 M (1)
description : 백트레킹
"""

def solution(N, M, now):
    if len(now) == M:
        print(*now)
        return

    for i in range(1, N + 1):
        if len(now) == 0:
            now.append(i)
            solution(N, M, now)
            now.pop()
        elif i not in now:
            now.append(i)
            solution(N, M, now)
            now.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M, [])
