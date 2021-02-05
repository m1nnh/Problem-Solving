"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 보물
description : 정렬
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0

for _ in range(N):
    result += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
print(result)
