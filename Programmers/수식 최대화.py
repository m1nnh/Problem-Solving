"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 수식 최대화
description : 구현
"""

from itertools import permutations
from collections import deque


def solution(expression):
    answer = 0

    list_op = ["+", "-", "*"]
    array = []
    string = ""
    for i in expression:
        if i.isdigit():
            string += i
        else:
            array.append(int(string))
            array.append(i)
            string = ""
    array.append(int(string))
    op = list(permutations(list_op, 3))

    for operation in op:
        queue = deque()
        total = 0
        for i in array:
            queue.append(i)
        for i in operation:
            length = len(queue)
            num_stack = []
            op_stack = []
            flag = False
            for j in range(length):
                now = queue.popleft()
                if str(type(now)) == "<class 'int'>":
                    if flag:
                        if i == "+":
                            total = int(now) + num_stack.pop()
                        elif i == "-":
                            total = num_stack.pop() - int(now)
                        else:
                            total = num_stack.pop() * int(now)
                        num_stack.append(total)
                    else:
                        num_stack.append(now)
                else:
                    if now == i:
                        flag = True
                    else:
                        op_stack.append(now)
                        flag = False

            length = len(num_stack)
            for k in range(length):
                if k + 1 != length:
                    queue.append(num_stack[k])
                    queue.append(op_stack[k])
                else:
                    queue.append(num_stack[k])
        answer = max(answer, abs(queue.popleft()))

    return answer
