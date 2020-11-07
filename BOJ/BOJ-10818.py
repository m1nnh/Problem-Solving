"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Max, Min
description : Math
"""

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()


print(n_list[0], n_list[-1])
