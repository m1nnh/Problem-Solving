"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Yangjojang of The Year
description : 정
"""

t = int(input())

for i in range(t):
    n = int(input())
    dic = dict()
    for _ in range(n):
        univ, score = map(str, input().split())
        dic[int(score)] = univ
    print(dic[max(dic.keys())])
