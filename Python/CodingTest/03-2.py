"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 큰 수의 법칙

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.

"""

N, M, K = map(int, input().split())

array = list(map(int, input().split()))
array.sort()

A = M % (K + 1)
sum_value = (array[-1] * K) + (array[-2])
result = (sum_value) * (M // (K + 1)) + (array[-1] * A)

print(result)
