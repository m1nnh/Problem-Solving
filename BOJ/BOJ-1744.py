"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 수 묶기
description : 그리디, 우선순위 큐
"""

import sys

input = sys.stdin.readline

n = int(input())

plusNumber = []
minusNumber = []
zeroNumber = []

for i in range(n):
    number = int(input())
    if number > 1:
        plusNumber.append(number)
    elif number < 0:
        minusNumber.append(number)
    else:
        zeroNumber.append(number)

plusNumber.sort(reverse=True)
minusNumber.sort()

result = 0
if len(plusNumber) % 2 == 0:
    for i in range(0, len(plusNumber) - 1, 2):
        result += plusNumber[i] * plusNumber[i + 1]
if len(plusNumber) % 2 != 0:
    for i in range(0, len(plusNumber) - 1, 2):
        result += plusNumber[i] * plusNumber[i + 1]
    result += plusNumber[-1]

if len(minusNumber) % 2 == 0:
    for i in range(0, len(minusNumber) - 1, 2):
        result += minusNumber[i] * minusNumber[i + 1]
if len(minusNumber) % 2 != 0:
    for i in range(0, len(minusNumber) - 1, 2):
        result += minusNumber[i] * minusNumber[i + 1]

    if 0 not in zeroNumber:
        result += minusNumber[-1]

result += sum(zeroNumber)
print(result)
