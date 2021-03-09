"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 로프
description : Greedy
"""

N = int(input())
w = []
result = 0

for i in range(N):
    w.append(int(input()))
w.sort(reverse=True)
count = 1

for i in w:
    result = max(result, i * count)
    count += 1
print(result)
