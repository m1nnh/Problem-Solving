"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 카드2
description : 자료구조, 큐
"""

from collections import deque

n = int(input())
num_list = [i + 1 for i in range(n)]
max_value = max(num_list)
card_list = deque()

for i in range(n):
    card_list.append([i, num_list[i]])

flag = True

if n == 1:
    flag = False
count = 1

while flag:
    del_idx, del_value = card_list.popleft()
    n -= 1
    if n == 1:
        flag = False
    else:
        push_idx, push_value = card_list.popleft()
        card_list.append([push_idx, push_value])
print(card_list[0][1])
