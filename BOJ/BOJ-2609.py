"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 최대공약수와 최소공배수
description : 수학, 정수론, 유클리드 호제법
"""


def GCM(num1, num2):
    max_value = max(num1, num2)
    min_value = min(num1, num2)
    a = 0
    if max_value % min_value == 0 or max_value == min_value:
        return min_value
    while max_value % min_value != 0:
        a = max_value % min_value
        max_value = min_value
        min_value = a
    return a


A, B = map(int, input().split())
print(GCM(A, B), round((A * B) / GCM(A, B)), sep='\n')
