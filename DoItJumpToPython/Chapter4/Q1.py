## 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성 해 보자.

def is_odd(n) :
    if n % 2 == 1 :
        return True
    else :
        return False

num = int(input("input number : "))

boolean = is_odd(num)

if boolean == True :
    print("odd")
else :
    print("even")