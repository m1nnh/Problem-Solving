"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 직각삼각형
description : 수학, 기하학
"""

while True:
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    if (a[0] ** 2) + (a[1] ** 2) == a[2] ** 2:
        print('right')
    else:
        print('wrong')
