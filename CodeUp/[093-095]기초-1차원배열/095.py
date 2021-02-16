""" 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.
    입력
    첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
    두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
    10
    10 4 2 3 6 6 7 9 8 5
    출력
    출석을 부른 번호 중에 가장 빠른 번호를 1개만 출력한다.
    2 """

import random

n = int(input())

randlist = []
for i in range(n) :
    rand=random.randint(1,23)
    randlist.append(rand)

print(*randlist)
print(min(randlist))

