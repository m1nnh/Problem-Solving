"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 나무 자르기
description : 이분 탐색
"""
import sys

N, M = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

H.sort()

start = 0
end = H[N - 1]
max_H = 0

while start <= end:
    get = 0
    mid = (start + end) // 2
    if mid != 0:
        for i in range(N):
            if H[i] // mid != 0:
                get += H[i] - mid

    if get >= M:
        max_H = max(max_H, mid)
        start = mid + 1
    else:
        end = mid - 1

print(max_H)
