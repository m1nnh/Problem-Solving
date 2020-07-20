"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : A+B - 7
description : Math
"""

t = int(input())
result = []
for i in range(t):
    a, b = map(int, input().split())
    result.append(a + b)
for i in range(t):
    print('Case #{}: {}'.format(i + 1, result[i]))
