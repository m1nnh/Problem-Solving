## 정수 3개를 입력받아 합과 평균을 출력해보자.

var = list(map(int, input().split()))

sum = 0

for i in range(len(var)) :
    sum += var[i]

print(sum)
print(round(sum/len(var),1))