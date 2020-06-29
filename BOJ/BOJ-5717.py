"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 상근이의 친구
description : 수학, 사칙연산
"""

m, f = map(int, input().split())

while m != 0 and f != 0:
    print(m + f)
    m, f = map(int, input().split())
