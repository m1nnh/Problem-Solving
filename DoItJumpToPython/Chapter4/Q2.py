## 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
## 단 입력으로 들어오는 수의 개수는 정해져 있지 않다.

def sum_avg(*num) :
    result = 0

    for i in num :
        result += i

    return result/len(num)

print(sum_avg(1,2))
print(sum_avg(1,2,3,4,5))