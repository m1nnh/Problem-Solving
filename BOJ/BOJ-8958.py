"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : O / X Quiz
description : Implementation
"""

test_num = int(input())

for i in range(test_num):
    score, count = 0, 0
    string = input()

    for ox in string:
        if ox == 'O':
            count += 1
        else:
            count = 0
        score += count
    print(score)
