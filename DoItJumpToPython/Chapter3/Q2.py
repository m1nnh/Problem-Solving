## while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

result = 0
i = 1

while i <= 1000 :
    if i % 3 == 0 :
        result = result + i
    i+=1

print(result)

