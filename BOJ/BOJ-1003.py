"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 피보나치 함수
description : 다이나믹 프로그래밍
"""

T = int(input())

result = [(1, 0), (0, 1)]

for i in range(2, 41):
    zero = result[i - 2][0] + result[i - 1][0]
    one = result[i - 2][1] + result[i - 1][1]
    result.append((zero, one))

for i in range(T):
    num = int(input())
    print(*result[num])
