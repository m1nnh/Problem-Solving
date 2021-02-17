"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 곱하기 혹은 더하기
description : 그리디
"""

S = input()
result = int(S[0])

for i in range(1, len(S)):
    if result == 0 or int(S[i]) == 0:
        result += int(S[i])
    else:
        result *= int(S[i])
print(result)
