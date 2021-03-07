"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 계수 정렬
description : 정렬
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 0, 5, 2]
count = [0] * (max(array) + 1)

for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
