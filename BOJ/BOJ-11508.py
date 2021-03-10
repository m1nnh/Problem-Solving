"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 2 + 1 세일
description : Greedy
"""

N = int(input())
Product = []
for i in range(N):
    Product.append(int(input()))
Product.sort(reverse=True)
Sum_Product = 0
count = 0
for i in range(N):
    if count == 2:
        count = 0
    else:
        count += 1
        Sum_Product += Product[i]
print(Sum_Product)
