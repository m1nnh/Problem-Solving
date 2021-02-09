"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 에너지 드링크
description : Greedy
"""

N = int(input())
Drink = list(map(int, input().split()))
Drink.sort(reverse=True)
Sum_Drink = Drink[0]

for i in range(1, N):
    Sum_Drink += Drink[i] / 2
print(Sum_Drink)
