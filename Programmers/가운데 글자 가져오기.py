"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 가운데 글자 가져오기
description : 문자열
"""


def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer += s[len(s) // 2 - 1]
    answer += s[len(s) // 2]
    return answer


if __name__ == '__main__':
    print(solution('abcde'))
    print(solution('qwer'))
