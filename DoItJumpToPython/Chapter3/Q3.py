## while문을 사용하여 다음과 같이 별을 찍어라.
## *
## **
## ***
## ****
## *****

i = 0

while i < 5 :
    j = 0
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1


