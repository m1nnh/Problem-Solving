"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 개표
description : 문자
"""

v=int(input())
a=input()
a_count=0
b_count=0

for i in range(len(a)):
    if a[i]=='A':
        a_count +=1
    else:
        b_count +=1

if a_count>b_count:
    print('A')
elif b_count>a_count:
    print('B')
else:
    print('Tie')
