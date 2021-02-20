"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 팩토리얼 0의 개수
description : 수학, 임의 정밀도/ 큰 수 연산
"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


N = int(input())

result = str(factorial(N))
count = 0
for i in range(len(result) - 1, 0, -1):
    if result[i] == '0':
        count += 1
    else:
        break
print(count)
