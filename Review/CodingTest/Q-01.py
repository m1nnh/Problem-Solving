"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 모험가 길드
description : 그리디
"""

N = int(input())
horror = list(map(int, input().split()))
horror.sort()
count = 0
result = 0
for i in horror:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
