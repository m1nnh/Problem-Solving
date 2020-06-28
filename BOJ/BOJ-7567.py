"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 그릇
description : 구현
"""

string = input()
h = 10

for i in range(1, len(string)):
    if string[i - 1] == string[i]:
        h += 5
    else:
        h += 10
print(h)
