"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 회의실 배정
description : Greedy
"""

N = int(input())
Time = []

for i in range(N):
    Time.append(list(map(int, input().split())))

Time.sort(key=lambda x: x[0])
Time.sort(key=lambda x: x[1])

count = 0
finish = 0

for i, j in Time:
    if i >= finish:
        count += 1
        finish = j
print(count)
