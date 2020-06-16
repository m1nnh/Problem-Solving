"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 스택 수열
description : 자료구조, 스택
"""

n = int(input())

a = []
b = []
s = []

num_list = []

count = 1

for i in range(n):
    num = int(input())
    num_list.append(num)
    while count <= num:
        a.append(count)
        s.append('+')
        count += 1
    if a[-1] == num:
        b.append(a.pop())
        s.append('-')

if num_list == b:
    [print(x) for x in s]
else:
    print('NO')
