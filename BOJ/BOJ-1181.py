"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 단어정렬
description : 문자열, 정렬
"""

t = int(input())
string = set()
for i in range(t):
    a = input()
    string.add(a)
b = list(string)
b.sort(key=lambda x: (len(x), x))

[print(x) for x in b]
