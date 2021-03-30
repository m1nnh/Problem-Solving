## 정수(1 ~ 100) 1개가 입력 되었을 때 카운트 다운을 출력해보자.
## 입력 : 정수 1개가 입력 된다. (1 ~ 100)
## 출력 : 1씩 줄이면서 한 줄에 하나씩 1이 될 때 까지 출력한다.

count = int(input())

for i in range(count) :

    print(count)

    count -= 1
    if count == 0 :
        break

