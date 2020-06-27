"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 약수들의 합
description : 수학, 정수론
"""

t = int(input())

while t != -1:
    num_list = []
    for i in range(1, t):
        if t % i == 0:
            num_list.append(i)
    if sum(num_list) == t:
        print('{} ='.format(t), end=' ')
        for i in range(len(num_list)):
            print('{}'.format(num_list[i]), end=' ')
            if len(num_list) - 1 > i:
                print('+', end=' ')
            else:
                print()
    else:
        print('{} is Not perfect.'.format(t))
    t = int(input())
