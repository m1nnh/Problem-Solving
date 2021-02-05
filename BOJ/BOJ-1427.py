"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 소트인사이드
description : 정렬
"""

N = input()
arr = []

for i in N:
    arr.append(int(i))

arr.sort(reverse=True)
[print(x, end='') for x in arr]
