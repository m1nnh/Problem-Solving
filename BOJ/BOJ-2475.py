"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Number of Verifications
description : Math
"""

list_num = list(map(int, input().split()))

result = 0

for i in list_num :
    result += i**2

print(result%10)

