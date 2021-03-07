"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 성적이 낮은 순서로 학생 출력하기
description : 정렬
"""

N = int(input())
array = {}
for i in range(N):
    A, B = map(str, input().split())
    array[int(B)] = A
array = sorted(array.items(), key=lambda x: x[0])

[print(array[x][1], end=' ') for x in range(len(array))]
