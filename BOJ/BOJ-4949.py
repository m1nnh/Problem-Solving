"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 균형잡힌 세상
description : 스택
"""

while True:
    String = input()
    dic = {')': '(', ']': '['}
    stack = []

    if String == '.':
        break

    for i in String:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if stack and stack[-1] == dic[i]:
                stack.pop()
            else:
                stack.append(i)

    if stack:
        print('no')
    else:
        print('yes')
