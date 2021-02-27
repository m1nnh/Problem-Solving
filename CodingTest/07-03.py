"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 이진 탐색(반복)
"""

N, S = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = len(array) - 1
result = True
mid = 0
while start <= end:
    mid = (start + end) // 2
    if array[mid] == S:
        result = False
        break
    elif array[mid] > S:
        end = mid - 1
    elif array[mid] < S:
        start = mid + 1

if result is True:
    print('존재하지 않습니다.')
else:
    print(mid + 1)
