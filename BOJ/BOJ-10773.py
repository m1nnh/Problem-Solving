"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 제로
description : 구현, 자료구조, 문자열, 스택
"""

K = int(input())
stack = []
for i in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))
