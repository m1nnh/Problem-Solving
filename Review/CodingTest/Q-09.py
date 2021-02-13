"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 압축
description : 구현
"""

S = input()

min_value = len(S)

for i in range(1, len(S) // 2 + 1):
    String = ""
    str_value = S[:i]
    count = 1

    for j in range(i, len(S), i):
        if str_value == S[j:j + i]:
            count += 1
        else:
            String += str(count) + str_value if count >= 2 else str_value
            str_value = S[j:j + i]
            count = 1
    String += str(count) + str_value if count >= 2 else str_value

    min_value = min(min_value, len(String))
print(min_value)
