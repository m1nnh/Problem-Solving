"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 블로그2
description : 그리디
"""

N = int(input())
Color = input()
Start = Color[0]
count = [1] * 3
ChangeB = 'B'
ChangeR = 'R'

for i in Color:
    if Start != i:
        count[0] += 1
        Start = i
    if i == 'R':
        if ChangeB == 'B':
            count[1] += 1
            ChangeB = 'R'
        ChangeR = 'R'
    else:
        if ChangeR == 'R':
            count[2] += 1
            ChangeR = 'B'
        ChangeB = 'B'

print(min(count))
