"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Find alphabet
description : Implementation
"""

s = input()

alphabet = [i for i in range(ord('a'), ord('z') + 1)]

for i in range(len(alphabet)):
    if chr(alphabet[i]) in s:
        idx = s.index(chr(alphabet[i]))
        alphabet[i] = idx
    else:
        alphabet[i] = -1
    print(alphabet[i], end=' ')
