"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 큰 수의 법칙
description : 그리디 알고리즘
"""

N, M, K = map(int, input().split())
Array = list(map(int, input().split()))
Result = 0

Array.sort(reverse=True)
for i in range(M):
    if i == 0 or i % K != 0:
        Result += Array[0]
    else:
        Result += Array[1]

print(Result)
