"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : The rest
description : Math
"""

result = set()

for i in range(10):
    num=int(input())
    result.add(num%42)

print(len(result))
