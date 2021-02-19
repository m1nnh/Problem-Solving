"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 시각
description : 구현
"""

N = int(input())
count = 0

for i in range(N + 1):
    for j in range(60):
        for k in range(60):

            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
