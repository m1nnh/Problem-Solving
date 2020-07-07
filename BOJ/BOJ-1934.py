"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최소공배수
description : 수학, 정수론, 유클리드 호제법
"""


def lcm(a, b):
    d = gcd(a, b)
    return d * (a // d) * (b // d)


def gcd(a, b):
    return gcd(b % a, a) if b % a else a


t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))
