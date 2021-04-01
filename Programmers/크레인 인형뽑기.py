"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 크레인 인형뽑기
description : 스택
"""


def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        result = 0
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                result = board[j][i - 1]
                board[j][i - 1] = 0
                break
        if result == 0:
            continue
        if not stack:
            stack.append(result)
        else:
            last = stack.pop()
            if last == result:
                answer += 2
            else:
                stack.append(last)
                stack.append(result)

    return answer
