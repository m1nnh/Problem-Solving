"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 내림차순으로 배치하기
description : 구현
"""

def solution(s):
    answer = ''.join(sorted(s, reverse = True))
    return answer