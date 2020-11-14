"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Musical scales
description : Implementation
"""

list_num = list(map(int, input().split()))
val = sorted(list_num)
if list_num == val :
    print("ascending")
elif list_num == val[::-1]:
    print("descending")
else:
    print("mixed")