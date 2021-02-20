"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 부녀회장이 될테야
description : 수학, 조합론
"""

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    a = [x for x in range(1, n+1)]

    for j in range(k):
        for y in range(1, n):
            a[y] += a[y-1]

    print(a[-1])