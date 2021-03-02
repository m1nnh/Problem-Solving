"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 잃어버린 괄호
description : 수학, 그리디 알고리즘, 문자열, 파싱
"""

cal = input()
sum_value = []
sub_value = []
i = 0
sum_temp = ""
sub_temp = ""
result = 0

while i < len(cal):
    if cal[i] == '+':
        sum_value.append(sum_temp)
        sum_temp = ""
        i += 1
    elif cal[i] == '-':
        if sum_temp != "":
            sum_value.append(sum_temp)
            sum_temp = ""
        i += 1
        for j in range(i, len(cal)):
            if cal[j] == '+':
                sub_value.append(sub_temp)
                sub_temp = ""
                i += 1
                continue
            elif cal[j] == '-':
                sub_value.append(sub_temp)
                sub_temp = ""
                break
            else:
                sub_temp += cal[j]
                i += 1
            if j == len(cal) - 1:
                sub_value.append(sub_temp)
                i += 1
    else:
        sum_temp += cal[i]
        i += 1
        if i == len(cal):
            sum_value.append(sum_temp)

for i in sum_value:
    result += int(i)
for j in sub_value:
    result -= int(j)
print(result)
