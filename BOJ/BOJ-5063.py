"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : TGN
description : 수학, 사칙연산
"""

t = int(input())

for i in range(t):
    r, e, c = map(int, input().split())
    if e>r+c:
        print('advertise')
    elif e<r+c:
        print('do not advertise')
    else:
        print('does not matter')
