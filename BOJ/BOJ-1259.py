"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 팰린드롬
description : 구현, 문자열
"""

num = list(map(int,input()))

while num[0]!=0:
    if num==num[::-1]:
        print('yes')
    else:
        print('no')
    num = list(map(int, input()))