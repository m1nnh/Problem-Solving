"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Multiplication
description : Math
"""

a = int(input())
b = int(input())

print(a * (b % 10))
print(a * ((b % 100) // 10))
print(a * (b // 100))
print(a * b)
