"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Repeat String
description : Implementation
"""

t = int(input())


for i in range(t) :
    p = []
    r, s = map(str, input().split())
    for j in range(len(s)) :
       p.append(s[j]*int(r))
    print(''.join(p))

