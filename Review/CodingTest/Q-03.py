"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 뒤집기
description : 그리디
"""

S = input()
zero_count = 0
one_count = 0

if S[0] == '1':
    zero_count += 1
else:
    one_count += 1

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        if S[i + 1] == '1':
            zero_count += 1
        else:
            one_count += 1
print(min(zero_count, one_count))
