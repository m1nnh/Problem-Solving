"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 괄호
description : 자료구조, 문자열, 스택
"""

T = int(input())
dic = {')': '('}

for i in range(T):
    stack = []
    String = input()
    for j in String:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack and stack[-1] == dic[j]:
                stack.pop()
            else:
                stack.append(j)
    if stack:
        print('NO')
    else:
        print('YES')
