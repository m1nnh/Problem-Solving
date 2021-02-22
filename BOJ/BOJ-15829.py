"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Hashing
description : 문자열, 해싱
"""

import sys

input = sys.stdin.readline

N = int(input())
string = input().rstrip()

result = 0
for i in range(len(string)):
    result += (ord(string[i]) - 96) * 31 ** i

print(result % 1234567891)
