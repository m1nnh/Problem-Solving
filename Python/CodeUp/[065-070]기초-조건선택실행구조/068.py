## 평가(정수, 0 ~ 100)을 입력 받아 평가를 출력해보자.
## 평가 기준 : 90 ~ 100 : A , 70 ~ 89 : B, 40 ~ 69 : C, 0 ~ 39 : D

grade = int(input())

if grade >= 90 :
    print("A")
elif grade >= 70 :
    print("B")
elif grade >= 40 :
    print("C")
else :
    print("D")

