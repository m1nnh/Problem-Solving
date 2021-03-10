"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 1, 2, 3 더하기
description : 다이나믹 프로그래밍
"""

n = int(input())
arr = [0, 1, 2, 4]

for i in range(4, 11):
    sum = arr[i - 1] + arr[i - 2] + arr[i - 3]
    arr.append(sum)

for i in range(n):
    num = int(input())
    print(arr[num])
