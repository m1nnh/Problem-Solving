"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 랜선 자르기
description : 이분 탐색
"""

k, n = map(int, input().split())
a = []

for i in range(k):
    a.append(int(input()))

start = 1
end = max(a)

result = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for j in range(k):
        count = count + (a[j] // mid)
    if count >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
