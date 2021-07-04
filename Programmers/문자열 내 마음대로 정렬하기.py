"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 내 마음대로 정렬하기
description : 정렬
"""

def solution(strings, n):
    answer = sorted(strings, key = lambda x : (x[n], x))
    return answer