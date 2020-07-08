"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 평균 점수
description : Math
"""

student = []
for i in range(5):
    student.append(int(input()))
    if student[i] < 40:
        student[i] = 40
print(int(sum(student) / 5))
