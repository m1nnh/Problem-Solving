"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Small factorization
description : Hydrostatic theory
"""

n = int(input())
s = []
i = 2
while n != 1:
    if n % i == 0:
        n //= i
        s.append(i)
    else:
        i += 1
for i in range(len(s)):
    print(s[i])
