"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 럭키 스트레이트
description : 구현
"""

N = int(input())
array = str(N)
result1 = 0
result2 = 0

for i in range(len(array)):
    if i < len(array) // 2:
        result1 += int(array[i])
    else:
        result2 += int(array[i])

if result1 == result2:
    print('LUCKY')
else:
    print('READY')
