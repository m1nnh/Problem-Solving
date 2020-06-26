"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 사분면
description : 수학, 구현
"""

t = int(input())
q = [0 for _ in range(4)]
a = 0
for i in range(t):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        a += 1
    elif x > 0:
        if y > 0:
            q[0] += 1
        else:
            q[3] += 1
    else:
        if y > 0:
            q[1] += 1
        else:
            q[2] += 1

for i in range(4):
    print('Q{}: {}'.format(i + 1, q[i]))
print('AXIS: {}'.format(a))
