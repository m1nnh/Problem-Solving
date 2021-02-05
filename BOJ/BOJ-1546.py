"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Average
description : Math
"""

n = int(input())
grade = [int(x) for x in input().split()]

max_grade = max(grade)
new_grade = [x/max_grade*100 for x in grade]

print(sum(new_grade)/n)

