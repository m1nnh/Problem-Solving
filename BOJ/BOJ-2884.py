"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Alarm clock
description : Math
"""

h, m = map(int, input().split())

if h==0 and m<45 :
    h += 23
    m = m+15
elif m<45 :
    h -= 1
    m = m+15
else :
    m = m-45

print('{} {}'.format(h,m))
