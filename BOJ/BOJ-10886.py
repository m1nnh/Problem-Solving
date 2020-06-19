"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 0 = not cute / 1 = cute
description : 수학, 구현, 사칙연
"""

n = int(input())
count = 0

for i in range(n):
    a = int(input())
    if a == 0:
        count += 1
if (n / 2) > count:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
