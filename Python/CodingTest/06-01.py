"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 선택 정렬
"""

N = int(input())
array = list(map(int, input().split()))
for i in range(N - 1):
    min_index = i
    for j in range(i + 1, N):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print(array)
