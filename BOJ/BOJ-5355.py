"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Mars math
description : Math
"""

t = int(input())
for i in range(t):
    mars = list(map(str, input().split()))
    result = float(mars[0])
    for j in range(1, len(mars)):
        if mars[j] == '@':
            result *= 3
        elif mars[j] == '%':
            result += 5
        else:
            result -= 7
    print('%0.2f' % result)
