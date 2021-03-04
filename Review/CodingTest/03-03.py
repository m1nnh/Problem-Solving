"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 숫자 카드 게임
description : 그리디 알고리즘
"""

N, M = map(int, input().split())
max_value = 0

for i in range(N):
    Array = list(map(int, input().split()))
    max_value = max(max_value, min(Array))

print(max_value)
