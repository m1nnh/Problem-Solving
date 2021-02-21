"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 소수 구하기
M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""

import math

M, N = map(int, input().split())
check = [True] * (N + 1)
check[0], check[1] = False, False

for i in range(2, int(math.sqrt(N)) + 1):
    if check[i] is True:
        for j in range(i * 2, N + 1, i):
            check[j] = False

for i in range(M, N):
    if check[i] is True:
        print(i, end=' ')
