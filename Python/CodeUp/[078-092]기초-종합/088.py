""" 3의 배수는 통과?
    1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성 하 되, 3의 배수인 경우는 출력하지 않도록 만들어 보자.
    입력 : 10
    출력 : 1 2 4 5 7 8 10 """

num = int(input())

for i in range(1,num+1) :
    if i%3 == 0 :
        continue
    else :
        print(i, end=' ')

