"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 비밀번호 찾기
description : 딕셔너리
"""

N, M = map(int, input().split())
dict = {}

for _ in range(N):
    site, password = map(str, input().split())
    dict[site] = password

for _ in range(M):
    site_address = input()
    print(dict[site_address])
