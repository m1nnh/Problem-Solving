"""
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 피보나치 함수 소스코드
description : 다이나믹 프로그래밍

"""

d = [0] * 100
d[1] = 1
d[2] = 1

for i in range(3, 100):
    d[i] = d[i - 1] + d[i - 2]

print(d[99])
