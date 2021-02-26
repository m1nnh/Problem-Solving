"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 키를 활용한 소스코드
"""

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

array.sort(key=lambda x: x[1])

print(array)
