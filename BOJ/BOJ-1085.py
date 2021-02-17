"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 직사각형에서 탈출
description : 수학, 기하학
"""

x, y, w, h = map(int, input().split())

print(min(abs(w - x), abs(h - y), abs(x), abs(y)))
