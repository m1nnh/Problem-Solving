"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 신입사원
description : 그리디
"""

T = int(input())

for _ in range(T):
    N = int(input())
    count = 1
    array = [list(map(int, input().split())) for _ in range(N)]
    array.sort()
    x = array[0][1]

    for i in range(1, N):
        if x > array[i][1]:
            count += 1
            x = array[i][1]
    print(count)
