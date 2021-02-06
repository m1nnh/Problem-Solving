"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Number Comparison
description : Math
"""

a, b = map(int, input().split())

if a > b :
    print('>')
elif a < b :
    print('<')
else :
    print('==')