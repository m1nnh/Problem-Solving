"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : A+B - 8
description : Math
"""

t = int(input())
a_list = []
result = []
for i in range(t):
    a, b = map(int, input().split())
    a_list.append(a)
    result.append(a + b)

for i in range(t):
    print('Case #{}: {} + {} = {}'.format(i + 1, a_list[i], result[i] - a_list[i], result[i]))
