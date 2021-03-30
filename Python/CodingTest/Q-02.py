"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 곱하기 혹은 더하기
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 대, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
예를 들어 02984라는 문자열이 주어지면, 만들어질 수 있는 가장 큰수는 ((((0 + 2) * 9) * 8) * 4) = 576입니다.
또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

description : 그리디 알고리즘
"""

import sys

input = sys.stdin.readline
S = input().rstrip()
result = int(S[0])

for i in range(1, len(S)):
    if result < 2 or int(S[i]) <= 1:
        result += int(S[i])
    else:
        result *= int(S[i])

print(result)
