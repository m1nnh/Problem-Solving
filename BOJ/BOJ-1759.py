"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 암호 만들기
description : 백트레킹
"""

from itertools import combinations

L, C = map(int, input().split())
String = sorted(list(map(str, input().split())))
vowel = ('a', 'e', 'i', 'o', 'u')

comb = list(combinations(String, L))

for now in comb:
    count = 0
    for i in now:
        if i in vowel:
            count += 1
    if (count >= 1) and (count <= L - 2):
        print(''.join(now))
