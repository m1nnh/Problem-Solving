"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 거스름돈
description : 그리디 알고리즘
"""

N = int(input())
Coin = [500, 100, 50, 10]
result = 0
for i in Coin:
    result += N // i
    N %= i

print(result)
