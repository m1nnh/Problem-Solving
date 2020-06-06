"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 분해합
description : 브루트포스 알고리즘
"""

n = input()
flag = False
min_value = int(1e9)
temp = '0'

if int(len(n)) == 1:
    print(0)
    exit()

for i in range(1, (int(len(n)) * 9) + 1):
    m = int(n) - i
    temp = str(m)
    for j in range((int(len(temp)))):
        m += int(temp[j])
    if m == int(n):
        min_value = min(min_value, int(temp))
        flag = True

if flag is True:
    print(min_value)
else:
    print(0)
