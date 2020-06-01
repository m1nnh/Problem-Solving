"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 설탕 배달
description : 수학, 다이나믹 프로그래밍, 그리디 알고리즘
"""

N = int(input())
flag = True
count5 = 0
count3 = 0
while flag:
    if N % 5 == 0:
        count5 += N // 5
        N = 0
    elif N % 8 == 0:
        N -= 8
        count5 += 1
        count3 += 1
    else:
        N -= 3
        count3 += 1

    if N == 0:
        print(count3 + count5)
        break
    elif N < 3:
        print(-1)
        break
