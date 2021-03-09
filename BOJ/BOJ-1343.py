"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com


title : 폴리오미노
description : Greedy
"""

Board = input()
new_Board = ""
A = "AAAA"
B = "BB"
flag = True
count = 0
for i in range(len(Board)):
    count += 1
    if Board[i] == '.' or i == len(Board) - 1:
        if Board[i] == '.':
            count -= 1
        while count != 0:
            if count // 4 >= 1:
                new_Board += A
                count -= 4
            elif count // 2 >= 1:
                new_Board += B
                count -= 2
            else:
                flag = False
                break
        if Board[i] == '.':
            new_Board += Board[i]

if flag:
    print(new_Board)
else:
    print(-1)
