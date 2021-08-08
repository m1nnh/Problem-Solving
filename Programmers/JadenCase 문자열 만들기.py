"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : JadenCase 문자열 만들기
description : 문자열
"""


def solution(s):
    answer = ""
    flag = True
    for st in s:
        if st == " ":
            flag = True
            answer += st
            continue

        if flag:
            flag = False
            if st.isalpha():
                answer += st.upper()
            else:
                answer += st
        else:
            answer += st.lower()

    return answer
