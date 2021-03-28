"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 별찍기
description : 재귀함수
"""

import math


def draw(cal):
    for i in range(len(stars)):
        stars.append(stars[i] + stars[i])
        stars[i] = ('   ' * cal + stars[i] + '   ' * cal)


stars = ['  *   ', ' * *  ', '***** ']
N = int(input())

iter = int(math.log(N // 3, 2))

for i in range(iter):
    draw(int(pow(2, i)))

for i in range(N):
    print(stars[i])
