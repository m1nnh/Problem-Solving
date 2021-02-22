"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 숫자 카드 2
description : 자료구조, 이분 탐색, 해시를 사용한 집합과 맵
"""

from collections import Counter

N = int(input())

Card_list = list(map(int, input().split()))

M = int(input())

Card = list(map(int, input().split()))

Card_counter = Counter(Card_list)

for i in Card:
    print(Card_counter[i], end=' ')
