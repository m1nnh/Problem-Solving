""" 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 대 나올 수 있는 모든 경우를 출력해보자.
    입력 : 2 3
    출력 : 1 1 1 2 1 3 2 1 2 ..."""

n, m = map(int,input().split())

for i in range(1,n+1) :
    for j in range(1,m+1) :
        print("%d %d" %(i,j))
