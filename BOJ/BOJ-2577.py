"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Number of Numbers
description : Math
"""

a=int(input())
b=int(input())
c=int(input())

list_str = str(a*b*c)

result = [0 for _ in range(10)]

for i in list_str :
    result[int(i)] +=1

for i in result :
    print(i)