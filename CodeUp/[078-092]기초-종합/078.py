## 짝수 합 구하기
## 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지의 짝수의 합을 구해보자.
## 입력 : 정수 1개가 입력된다. (0 ~ 100)

num = int(input())

sum = 0

for i in range(2,num+1,+2) :
    sum += i

print("sum = %d" %sum)