"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 뒤집기
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있습니다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 합니다.
다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것입니다. 뒤집는것은 1을 0으로, 0을 1로 바꾸는 것을 의미합니다.
예를들어 S = 0001100일 때는 다음과 같습니다.
    1. 전체를 뒤집으면 1110011이 됩니다.
    2. 4번째 문자부터 5번째 문자까지 뒤집으면 11111111이 되어서 두 번 만에 모두 같은 숫자로 만들 수 있습니다.
하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 00000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있습니다.
문자열 S가 주어졌을 때, 다솜이가 해야 하는 행동의 최소 횟수를 출력하세요.
description : 그리디 알고리즘
"""

import sys

input = sys.stdin.readline

S = list(input().rstrip())
count = 0
A = S[0]

for i in range(1, len(S)):
    if A != S[i] and S[i] != S[i - 1]:
        count += 1

print(count)