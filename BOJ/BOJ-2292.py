"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 벌집
description : 수
"""

n = int(input())

boundary = 1
step = 1

while True:
    if n <= boundary:
        break
    boundary += step*6
    step += 1
print(step)
