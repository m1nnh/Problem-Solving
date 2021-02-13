"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 재정렬
description : 구현
"""

S = input()
result = 0
String = []
for i in S:
    if i.isdigit():
        result += int(i)
    else:
        String.append(i)
String.sort()

print(''.join(String) + str(result))
