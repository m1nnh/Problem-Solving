"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 과자
description : 수학, 사칙연
"""

k, n, m = map(int, input().split())

if k * n > m:
    print(k * n - m)
else:
    print(0)
