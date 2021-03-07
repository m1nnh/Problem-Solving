"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 위에서 아래로
description : 정렬
"""

N = int(input())

array = []

for i in range(N):
    array.append(int(input()))

array.sort(reverse=True)

print(array)
