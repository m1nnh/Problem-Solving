"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 후위 표기식
description : 스택
"""

S = list(input())

result = ''

alpha = []
operation = []

while S:
    temp = S.pop(0)

    if temp.isalpha():
        result += temp
    else:
        if temp == '(':
            operation.append(temp)

        elif temp == '*' or temp == '/':
            while operation and (operation[-1] == '*' or operation[-1] == '/'):
                result += operation.pop()
            operation.append(temp)

        elif temp == '+' or temp == '-':
            while operation and operation[-1] != '(':
                result += operation.pop()
            operation.append(temp)
        elif temp == ')':
            while operation and operation[-1] != '(':
                result += operation.pop()
            operation.pop()
while operation:
    result += operation.pop()

print(result)
