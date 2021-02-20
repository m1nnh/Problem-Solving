"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Leap year
description : Math
"""

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)
