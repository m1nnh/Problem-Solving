"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Studying word
description : String
"""

from collections import Counter

string = input()
string = string.upper()

str = Counter(string)
result = str.most_common(2)

if len(result) == 1:
    print(result[0][0])
elif result[0][1] == result[1][1] :
    print("?")
else:
    print(result[0][0])


