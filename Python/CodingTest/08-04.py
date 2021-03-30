"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 반복적인 피보나치 수열
"""

array = [0] * 100

array[1] = 1
array[2] = 1
n = 99

for i in range(3, n + 1):
    array[i] = array[i - 1] + array[i - 2]
print(array[n])
