"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 성적이 낮은 순서로 학생 출력하기
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
"""

N = int(input())
array = []

for i in range(N):
    A = list(map(str, input().split()))
    array.append(A)

array.sort(key=lambda x: int(x[1]))  # array = sorted(array, key=lambda x : int(x[1]))

for i in array:
    print(i[0], end=' ')
