"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 팰린드롬인지 확인하기
description : 구현, 문자
"""

string = input()
string_reverse = string[::-1]
if string == string_reverse:
    print(1)
else:
    print(0)
