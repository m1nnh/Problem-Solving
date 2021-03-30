"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 순차 탐색
"""

input_data = input().split()
array = list(map(str, input().split()))
count = 0
for i in array:
    count += 1
    if input_data[1] == i:
        print(count)
        break
