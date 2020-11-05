"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Number less tha x
description : Math
"""

n, x = map(int,input().split())
n_list = list(map(int,input().split()))

for i in n_list:
    if x>i :
        print(i,end=' ')