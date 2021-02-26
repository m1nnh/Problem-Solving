"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 피보나치 함수
"""


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if array[x] != 0:
        return array[x]
    array[x] = fibo(x - 1) + fibo(x - 2)
    return array[x]


array = [0] * 100
print(fibo(99))
