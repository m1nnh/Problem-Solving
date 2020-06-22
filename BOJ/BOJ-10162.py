"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 전자레인지
description : 수학, 구현, 사칙연산
"""

t = int(input())

if t % 10 != 0:
    print(-1)
else:
    A = t // 300
    B = (t % 300) // 60
    C = (t % 300) % 60 // 10
    print(A, B, C)
