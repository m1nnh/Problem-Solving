"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 나는야 포켓몬 마스터 이다솜
description : 자료 구조, 문자열, 해시를 사용한 집합과 맵
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
digit = dict()
alpha = dict()

for i in range(1, N + 1):
    name = input().rstrip()
    digit[i] = name
    alpha[name] = i

for j in range(M):
    A = input().rstrip()
    if A.isdigit():
        print(digit[int(A)])
    else:
        print(alpha[A])
