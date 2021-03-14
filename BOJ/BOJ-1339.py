"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 단어 수학
description : 그리디
"""

N = int(input())
array = []
dic = {}
for i in range(N):
    array.append(input())

for i in array:
    count = 0
    for j in i:

        if j not in dic:
            dic[j] = 10 ** (len(i) - count - 1)
        elif j in dic:
            dic[j] += 10 ** (len(i) - count - 1)
        count += 1

dic_list = sorted(list(dic.values()), reverse=True)
sum_value = 0

for i in range(len(dic_list)):
    sum_value += dic_list[i] * (9 - i)

print(sum_value)
