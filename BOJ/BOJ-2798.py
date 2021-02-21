"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 블랙잭
description : 브루트포스 알고리즘
"""

n, m = map(int, input().split())

a = list(map(int, input().split()))

value = 0
result = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            value = a[i] + a[j] + a[k]
            if value <= m:
                result = max(result, value)
print(result)
